import logging

from .db import init_db
from .campaign.resource import CampaignListResource, CampaignItemResource
from .campaign.services import build_campaign_service

logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        logger.info('power_dialer plugin loading')
        api = dependencies['api']
        init_db('postgresql://asterisk:proformatique@localhost/asterisk?application_name=wazo-power_dialer-plugin')
        campaign_service = build_campaign_service()

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

        logger.info('power_dialer plugin loaded')
