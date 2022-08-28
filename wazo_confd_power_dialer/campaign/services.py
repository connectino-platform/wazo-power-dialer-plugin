import traceback
from datetime import datetime

from wazo_confd.helpers.resource import CRUDService
from wazo_confd.plugins.application.service import build_service as build_application_service
from xivo_dao.helpers.db_manager import Session

from . import dao
import logging
from .notifier import build_campaign_notifier
from .validator import build_campaign_validator
from ..campaign_contact_call.model import CampaignContactCallModel
from ..campaign_contact_call.services import build_campaign_contact_call_service
from ..contact_list.services import build_contact_list_service

logger = logging.getLogger(__name__)


def build_campaign_service(auth_client, calld_client, confd_client):
    return CampaignService(
        auth_client,
        calld_client,
        confd_client,
        build_application_service(),
        build_campaign_contact_call_service(),
        build_contact_list_service(),
        dao,
        build_campaign_validator(),
        build_campaign_notifier()
    )


class CampaignService(CRUDService):

    def __init__(self,
                 auth_client, calld_client, confd_client,
                 application_service, campaign_contact_call_service, contact_list_service,
                 dao, validator, notifier,
                 extra_parameters=None):
        self.application_service = application_service
        self.campaign_contact_call_service = campaign_contact_call_service
        self.contact_list_service = contact_list_service
        self.auth_client = auth_client
        self.calld_client = calld_client
        self.confd_client = confd_client
        token = self.auth_client.token.new(expiration=365 * 24 * 60 * 60)['token']
        self.calld_client.set_token(token)
        self.confd_client.set_token(token)
        super().__init__(dao, validator, notifier, extra_parameters)

    def start(self, campaign_uuid):
        campaign = self.get_by(uuid=campaign_uuid)
        application = self.create_application(campaign.tenant_uuid)
        campaign.application_uuid = application["uuid"]
        campaign.state = "start"
        self.edit(campaign)
        self.commit()
        self.create_empty_campaign_contact_call(campaign)
        self.make_next_application_call(application["uuid"])
        return application

    def pause(self):
        pass

    def resume(self):
        pass

    def stop(self):
        pass

    def application_call_answered(self, event):
        self.play_music(event["application_uuid"], event["call"]["id"])

    def application_playback_created(self, event):
        pass

    def application_playback_deleted(self, event):
        self.hangup_application_call(event["application_uuid"])

    def application_call_deleted(self, event):
        self.make_next_application_call(event["application_uuid"])

    def find_next_campaign_contact_call(self, application_uuid):
        campaign = self.get_by(application_uuid=application_uuid)
        last_call = self.campaign_contact_call_service.search({
            "campaign_uuid": campaign.uuid,
            "make_call": None,
            "limit": 1
        })
        if last_call.total:
            return last_call.items[0]
        else:
            return None

    def get_application(self, tenant_uuid):
        application_name = self.generate_application_name(tenant_uuid)
        already_created_application = self.application_service.find_by(name=application_name)

        if already_created_application:
            return already_created_application

        return self.create_application(tenant_uuid)

    def create_application(self, tenant_uuid):
        application_name = self.generate_application_name(tenant_uuid)
        application_args = {
            "name": application_name,
            "destination": "node",
            "destination_options": {
                "answer": True,
                "music_on_hold": "",
                "type": "holding"
            }
        }
        self.confd_client.tenant_uuid = tenant_uuid
        return self.confd_client.applications.create(application_args)

    def generate_application_name(self, tenant_uuid):
        return f"{tenant_uuid}_campaign"

    def create_empty_campaign_contact_call(self, campaign):
        campaign_contact_call_canceled = self.campaign_contact_call_service.search({
            "campaign_uuid": campaign.uuid,
            "make_call": None
        })
        if campaign_contact_call_canceled.total:
            for campaign_contact_call in campaign_contact_call_canceled.items:
                self.campaign_contact_call_service.delete(campaign_contact_call)

        for contact_list in campaign.contact_lists:
            contact_list_with_contacts = self.contact_list_service.get_by(uuid=contact_list.uuid)
            for contact in contact_list_with_contacts.contacts:
                campaign_contact_call = CampaignContactCallModel()
                campaign_contact_call.phone = contact.phone
                campaign_contact_call.campaign_uuid = campaign.uuid
                campaign_contact_call.contact_list_uuid = contact_list.uuid
                campaign_contact_call.contact_uuid = contact.uuid
                self.campaign_contact_call_service.create(campaign_contact_call)

        Session.commit()

    def make_next_application_call(self, application_uuid, context="internal"):
        campaign_contact_call = self.find_next_campaign_contact_call(application_uuid)
        if campaign_contact_call is None:
            return

        campaign_contact_call.make_call = datetime.now()
        self.campaign_contact_call_service.edit(campaign_contact_call)
        self.commit()

        call_args = {
            "autoanswer": True,
            "context": context,
            "displayed_caller_id_name": "Milad Razban",
            "displayed_caller_id_number": "161",
            "exten": campaign_contact_call.phone,
            "variables": {}
        }
        try:
            call = self.calld_client.applications.make_call(application_uuid, call_args)
            return call
        except:
            logging.error(traceback.format_exc())

    def hangup_application_call(self, application_uuid):
        calls = self.calld_client.applications.list_calls(application_uuid)
        if calls.items:
            for call in calls["items"]:
                self.calld_client.applications.hangup_call(application_uuid, call["id"])

    def play_music(self, application_uuid, call_id):
        playback = {
            "uri": "sound:/var/lib/wazo/sounds/tenants/501ec54b-aa48-4492-bc5c-7af59c20705f/campaign/campagin_test"
        }
        playback = self.calld_client.applications.send_playback(application_uuid, call_id, playback)
        return playback

    def commit(self):
        try:
            Session.commit()
        except:
            Session.rollback()
            logging.error(traceback.format_exc())
