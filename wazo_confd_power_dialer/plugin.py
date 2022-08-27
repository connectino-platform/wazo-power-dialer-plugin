import logging

from wazo_calld_client import Client as CalldClient
from wazo_auth_client import Client as AuthClient
from .campaign.bus_consume import CampaignBusEventHandler
from .db import init_db
from .campaign.resource import CampaignListResource, CampaignItemResource, CampaignRunnerResource
from .campaign.services import build_campaign_service
from .contact.services import build_contact_service
from .contact_list.services import build_contact_list_service
from .contact.resource import ContactListResource, ContactItemResource, ContactImportResource
from .contact_list.resource import ContactListListResource, ContactListItemResource
from .contact_contact_list.resource import ContactContactListListResource
from .contact_contact_list.services import build_contact_contact_list_service
from .campaign_contact_list.resource import CampaignContactListListResource
from .campaign_contact_list.services import build_campaign_contact_list_service

logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        logger.info('power_dialer plugin loading')
        api = dependencies['api']
        auth_client = AuthClient(host='127.0.0.1', username='root', password='12345', verify_certificate=False,
                                 https=True)
        calld_client = CalldClient(host='127.0.0.1', port=443, verify_certificate=False, https=True)
        init_db('postgresql://asterisk:proformatique@localhost/asterisk?application_name=wazo-power_dialer-plugin')
        campaign_service = build_campaign_service(auth_client, calld_client)
        contact_service = build_contact_service()
        contact_list_service = build_contact_list_service()
        contact_contact_list_service = build_contact_contact_list_service()
        campaign_contact_list_service = build_campaign_contact_list_service()
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
            CampaignRunnerResource,
            '/powerdialer/campaigns/<uuid:uuid>/start',
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

        logger.info('power_dialer plugin loaded')
