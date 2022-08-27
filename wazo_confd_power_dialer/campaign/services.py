from flask import request
from wazo_confd.helpers.resource import CRUDService
from wazo_confd.plugins.application.schema import ApplicationSchema
from wazo_confd.plugins.application.service import build_service as build_application_service
from xivo_dao.alchemy import Application

from . import dao
import logging
from .notifier import build_campaign_notifier
from .validator import build_campaign_validator

logger = logging.getLogger(__name__)


def build_campaign_service(auth_client, calld_client):
    return CampaignService(
        auth_client,
        calld_client,
        build_application_service(),
        dao,
        build_campaign_validator(),
        build_campaign_notifier()
    )


class CampaignService(CRUDService):

    def __init__(self, auth_client, calld_client, application_service, dao, validator, notifier, extra_parameters=None):
        self.application_service = application_service
        self.auth_client = auth_client
        self.calld_client = calld_client
        super().__init__(dao, validator, notifier, extra_parameters)

    def init_clients(self):
        pass
        # token = request.headers.get('X-Auth-Token')
        token = self.auth_client.token.new(expiration=60)['token']
        self.calld_client.set_token(token)

    def get_application(self, tenant_uuid):
        application_name = f"{tenant_uuid}_campaign"
        already_created_application = self.application_service.find_by(name=application_name)

        if already_created_application:
            return already_created_application

        application = ApplicationSchema().load({
            "name": application_name,
            "destination": "node",
            "destination_options": {
                "answer": True,
                "music_on_hold": "",
                "type": "holding"
            }
        })
        application['tenant_uuid'] = tenant_uuid
        return self.application_service.create(Application(**application))

    def make_application_call(self, application_uuid):
        self.init_clients()
        call_args = {
            "autoanswer": True,
            "context": "internal",
            "displayed_caller_id_name": "Milad Razban",
            "displayed_caller_id_number": "161",
            "exten": "100",
            "variables": {}
        }
        call = self.calld_client.applications.make_call(application_uuid, call_args)
        return call

    def hangup_application_call(self, application_uuid):
        self.init_clients()
        calls = self.calld_client.applications.list_calls(application_uuid)
        logger.warning(calls)
        if calls.items:
            for call in calls["items"]:
                self.calld_client.applications.hangup_call(application_uuid, call["id"])

    def play_music(self, application_uuid, call_id):
        self.init_clients()
        playback = {
            "uri": "sound:/var/lib/wazo/sounds/tenants/501ec54b-aa48-4492-bc5c-7af59c20705f/campaign/campagin_test"
        }
        playback = self.calld_client.applications.send_playback(application_uuid, call_id, playback)
        return playback
