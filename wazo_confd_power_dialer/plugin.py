import logging

from wazo_calld_client import Client as CalldClient
from wazo_auth_client import Client as AuthClient
from wazo_confd_client import Client as ConfdClient
from .campaign.bus_consume import CampaignBusEventHandler
from .campaign_contact_call.resource import CampaignContactCallListResource, CampaignContactCallItemResource
from .db import init_db
from .campaign.resource import CampaignListResource, CampaignItemResource, CampaignStartResource, CampaignStopResource
from .campaign.resource import CampaignPauseResource, CampaignResumeResource
from .campaign.services import build_campaign_service
from .contact.services import build_contact_service
from .contact_list.services import build_contact_list_service
from .contact.resource import ContactListResource, ContactItemResource, ContactImportResource
from .contact_list.resource import ContactListListResource, ContactListItemResource
from .contact_contact_list.resource import ContactContactListListResource
from .contact_contact_list.services import build_contact_contact_list_service
from .campaign_contact_list.resource import CampaignContactListListResource
from .campaign_contact_list.services import build_campaign_contact_list_service
from .campaign_contact_call.services import build_campaign_contact_call_service

logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        logger.info('power_dialer plugin loading')
        api = dependencies['api']
        config = dependencies['config']
        auth_client = AuthClient(host='127.0.0.1', username='root', password='12345', verify_certificate=False,
                                 https=True)
        calld_client = CalldClient(host='127.0.0.1', port=443, verify_certificate=False, https=True)
        confd_client = ConfdClient(host='127.0.0.1', port=443, verify_certificate=False, https=True)
        init_db('postgresql://asterisk:proformatique@localhost/asterisk?application_name=wazo-power_dialer-plugin')
        campaign_service = build_campaign_service(auth_client, calld_client, confd_client)
        contact_service = build_contact_service()
        contact_list_service = build_contact_list_service()
        contact_contact_list_service = build_contact_contact_list_service()
        campaign_contact_list_service = build_campaign_contact_list_service()
        campaign_contact_call_service = build_campaign_contact_call_service()
        bus_consumer = dependencies['bus_consumer']
        bus_event_handler = CampaignBusEventHandler(campaign_service)
        bus_event_handler.subscribe(bus_consumer)

        # Campaigns
        api.add_resource(
            CampaignListResource,
            '/powerdialer/campaigns',
            resource_class_args=(campaign_service,)
        )
        api.add_resource(
            CampaignItemResource,
            '/powerdialer/campaigns/<uuid:uuid>',
            endpoint='powerdialer_campaigns',
            resource_class_args=(campaign_service,)
        )
        api.add_resource(
            CampaignStartResource,
            '/powerdialer/campaigns/<uuid:uuid>/start',
            resource_class_args=(campaign_service,)
        )
        api.add_resource(
            CampaignStopResource,
            '/powerdialer/campaigns/<uuid:uuid>/stop',
            resource_class_args=(campaign_service,)
        )
        api.add_resource(
            CampaignPauseResource,
            '/powerdialer/campaigns/<uuid:uuid>/pause',
            resource_class_args=(campaign_service,)
        )
        api.add_resource(
            CampaignResumeResource,
            '/powerdialer/campaigns/<uuid:uuid>/resume',
            resource_class_args=(campaign_service,)
        )
        # Contacts
        api.add_resource(
            ContactListResource,
            '/powerdialer/contacts',
            resource_class_args=(contact_service,)
        )
        api.add_resource(
            ContactItemResource,
            '/powerdialer/contacts/<uuid:uuid>',
            endpoint='powerdialer_contacts',
            resource_class_args=(contact_service,)
        )
        api.add_resource(
            ContactImportResource,
            '/powerdialer/contacts/import/contact-lists/<uuid:contact_list_uuid>',
            resource_class_args=(contact_service,)
        )

        # Contact lists
        api.add_resource(
            ContactListListResource,
            '/powerdialer/contact-lists',
            resource_class_args=(contact_list_service,)
        )
        api.add_resource(
            ContactListItemResource,
            '/powerdialer/contact-lists/<uuid:uuid>',
            endpoint='powerdialer_contact_lists',
            resource_class_args=(contact_list_service,)
        )

        # Contact <=> Contact list
        api.add_resource(
            ContactContactListListResource,
            '/powerdialer/contact-lists/<uuid:contact_list_uuid>/contact/<uuid:contact_uuid>',
            endpoint='powerdialer_contact_contact_lists',
            resource_class_args=(contact_contact_list_service,)
        )

        # Campaign <=> Contact list
        api.add_resource(
            CampaignContactListListResource,
            '/powerdialer/campaigns/<uuid:campaign_uuid>/contact-lists/<uuid:contact_list_uuid>',
            endpoint='powerdialer_campaigns_contact_lists',
            resource_class_args=(campaign_contact_list_service,)
        )

        # Campaign Contact Call
        api.add_resource(
            CampaignContactCallListResource,
            '/powerdialer/campaign-contact-calls',
            resource_class_args=(campaign_contact_call_service,)
        )
        api.add_resource(
            CampaignContactCallItemResource,
            '/powerdialer/campaign-contact-calls/<uuid:uuid>',
            endpoint='powerdialer_campaign_contact_calls',
            resource_class_args=(campaign_contact_call_service,)
        )

        logger.info('power_dialer plugin loaded')
