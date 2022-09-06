import logging

from xivo.pubsub import CallbackCollector

from .campaign.stasis import CampaignStasis

logger = logging.getLogger(__name__)


class Plugin:
    def load(self, dependencies):
        logger.info('calld_power_dialer plugin loading')

        ari = dependencies['ari']
        stasis = CampaignStasis(ari)
        startup_callback_collector = CallbackCollector()
        ari.client_initialized_subscribe(startup_callback_collector.new_source())
        startup_callback_collector.subscribe(stasis.initialize)

        logger.info('calld_power_dialer plugin loaded')
