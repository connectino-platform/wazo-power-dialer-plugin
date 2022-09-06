import logging

from wazo_calld.plugins.applications.stasis import AppNameHelper

logger = logging.getLogger(__name__)


class CampaignStasis:
    _app_name = 'campaign'

    def __init__(self, ari):
        logger.warning('========>x3<===========')
        self._ari = ari.client
        self._core_ari = ari

    def initialize(self):
        self._subscribe()
        self._add_ari_application()
        logger.warning('========>x1<===========')

    def _subscribe(self):
        self._ari.on_channel_event('ChannelStateChange', self.channel_state_change)
        logger.warning('========>x2<===========')

    def _add_ari_application(self):
        self._core_ari.register_application(self._app_name)

    def channel_state_change(self, channel, event):
        logger.warning('========>channel_state_change<===========')
        logger.warning(event)
        application_uuid = AppNameHelper.to_uuid(event.get('application'))
