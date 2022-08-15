import logging

from .db import init_db
from .campaign.resource import CampaignListResource, CampaignItemResource
from .campaign.services import build_campaign_service
from .contact.services import build_contact_service
from .contact_list.services import build_contact_list_service
from .contact.resource import ContactListResource, ContactItemResource
from .contact_list.resource import ContactListListResource, ContactListItemResource

logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        logger.info('power_dialer plugin loading')
        api = dependencies['api']
        init_db('postgresql://asterisk:proformatique@localhost/asterisk?application_name=wazo-power_dialer-plugin')
        campaign_service = build_campaign_service()
        contact_service = build_contact_service()
        contact_list_service = build_contact_list_service()

        # Campaigns
        api.add_resource(
            CampaignListResource,
            '/campaigns',
            resource_class_args=(campaign_service,)
        )
        api.add_resource(
            CampaignItemResource,
            '/campaigns/<uuid:uuid>',
            endpoint='campaigns',
            resource_class_args=(campaign_service,)
        )

        # Campaign contacts
        api.add_resource(
            ContactListResource,
            '/campaigns/contacts',
            resource_class_args=(contact_service,)
        )
        api.add_resource(
            ContactItemResource,
            '/campaigns/contacts/<uuid:uuid>',
            endpoint='campaigns_contacts',
            resource_class_args=(contact_service,)
        )

        # Campaign contacts list
        api.add_resource(
            ContactListListResource,
            '/campaigns/contact-lists',
            resource_class_args=(contact_list_service,)
        )
        api.add_resource(
            ContactListItemResource,
            '/campaigns/contact-lists/<uuid:uuid>',
            endpoint='campaigns_contact_lists',
            resource_class_args=(contact_list_service,)
        )

        logger.info('power_dialer plugin loaded')
