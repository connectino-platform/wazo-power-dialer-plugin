import logging

logger = logging.getLogger(__name__)


class CampaignBusEventHandler:
    def __init__(self, service):
        self._service = service

    def subscribe(self, bus_consumer):
        bus_consumer.on_event('application_call_answered', self._application_call_answered)
        bus_consumer.on_event('application_playback_deleted', self._application_playback_deleted)
        bus_consumer.on_event('application_call_deleted', self._application_call_deleted)
        bus_consumer.on_event('application_playback_created', self._application_playback_created)

    def _application_call_answered(self, event):
        logger.warning('========>application_call_answered<===========')
        logger.warning(event)
        # {'application_uuid': '7d48038a-fede-4554-8ae0-1d0df26ff232', 'call': {'id': '1661325098.15', 'moh_uuid': None,
        # 'caller_id_number': '161', 'tenant_uuid': None, 'dialed_extension': '100',
        # 'node_uuid': '424f3c3b-3997-4932-8324-4f9e42f438eb', 'muted': False, 'snoops': {}, 'status': 'Up',
        # 'creation_time': '2022-08-24T03:11:38.007-0400', 'caller_id_name': 'Milad Razban', 'user_uuid': None,
        # 'is_caller': True, 'on_hold': False}}
        campaign_engine = self._service.create_campaign_engine()
        campaign_engine.application_call_answered(event)

    def _application_playback_created(self, event):
        logger.warning('========>application_playback_created<===========')
        logger.warning(event)

        campaign_engine = self._service.create_campaign_engine()
        campaign_engine.application_playback_created(event)

    def _application_playback_deleted(self, event):
        logger.warning('========>application_playback_deleted<===========')
        logger.warning(event)
        # {'application_uuid':'7d48038a-fede-4554-8ae0-1d0df26ff232',
        # 'playback':{'uri':'sound:/var/lib/wazo/sounds/tenants/501ec54b-aa48-4492-bc5c-7af59c20705f/campaign/campagin_test',
        # 'uuid': 'c3a0beff-67f8-4297-8fed-fac9fa3c6728', 'language': 'en'}}
        campaign_engine = self._service.create_campaign_engine()
        campaign_engine.application_playback_deleted(event)

    def _application_call_deleted(self, event):
        logger.warning('========>application_call_deleted<===========')
        logger.warning(event)
        # {'application_uuid': '7d48038a-fede-4554-8ae0-1d0df26ff232', 'call': {'id': '1661578551.87', 'moh_uuid': None,
        # 'caller_id_number': '100', 'tenant_uuid': None, 'dialed_extension': None, 'node_uuid': None, 'muted': False,
        # 'snoops': {}, 'status': 'Up', 'creation_time': '2022-08-27T01:35:51.041-0400', 'caller_id_name': 'test1',
        # 'user_uuid': None, 'is_caller': False, 'on_hold': False}}
        campaign_engine = self._service.create_campaign_engine()
        campaign_engine.application_call_deleted(event)
