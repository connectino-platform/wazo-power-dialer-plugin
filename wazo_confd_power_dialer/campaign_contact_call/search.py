from xivo_dao.resources.utils.search import SearchConfig
from xivo_dao.resources.utils.search import SearchSystem

from .model import CampaignContactCallModel

campaign_contact_call_config = SearchConfig(
    table=CampaignContactCallModel,
    columns={
        'uuid': CampaignContactCallModel.uuid,
        'phone': CampaignContactCallModel.phone,
        'make_call': CampaignContactCallModel.make_call,
        'call_answered': CampaignContactCallModel.call_answered,
        'playback_created': CampaignContactCallModel.playback_created,
        'playback_deleted': CampaignContactCallModel.playback_deleted,
        'call_deleted': CampaignContactCallModel.call_deleted,
        'campaign_uuid': CampaignContactCallModel.campaign_uuid,
        'contact_list_uuid': CampaignContactCallModel.contact_list_uuid,
        'contact_uuid': CampaignContactCallModel.contact_uuid,
    },
    default_sort='make_call',
)

campaign_contact_call_search = SearchSystem(campaign_contact_call_config)
