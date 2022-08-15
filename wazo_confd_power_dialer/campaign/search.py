from xivo_dao.resources.utils.search import SearchConfig
from xivo_dao.resources.utils.search import SearchSystem

from .model import CampaignModel

campaign_config = SearchConfig(
    table=CampaignModel,
    columns={
        'uuid': CampaignModel.uuid,
        'name': CampaignModel.name,
    },
    default_sort='name',
)

campaign_search = SearchSystem(campaign_config)
