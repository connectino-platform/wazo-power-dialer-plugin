import logging

from wazo_calld.plugins.applications.stasis import AppNameHelper

logger = logging.getLogger(__name__)


class CampaignStasis:
    _app_name = 'power_dialer_campaign'

    def __init__(self, ari):
        self._ari = ari.client
        self._core_ari = ari

    def initialize(self):
        self._subscribe()
        self._add_ari_application()

    def _subscribe(self):
        self._ari.on_channel_event('ChannelStateChange', self.channel_state_change)
        self._ari.on_channel_event('StasisStart', self.stasis_start)
        self._ari.on_channel_event('StasisEnd', self.stasis_end)

    def channel_state_change(self, channel, event):
        logger.warning('========channel_state_change=XAXX==========')
        logger.warning(event)
        logger.warning(channel)
        application_uuid = AppNameHelper.to_uuid(event.get('application'))

    def stasis_end(self, channel, event):
        logger.warning('========stasis_end=XAXX==========')
        logger.warning(event)
        logger.warning(channel)
        application_uuid = AppNameHelper.to_uuid(event.get('application'))

    def stasis_start(self, event_objects, event):
        logger.warning('========stasis_start=XAXX==========')
        logger.warning(event)
        logger.warning(event_objects)

    def _add_ari_application(self):
        self._core_ari.register_application(self._app_name)
