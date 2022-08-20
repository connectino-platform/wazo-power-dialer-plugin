from xivo_dao.resources.utils.search import SearchConfig
from xivo_dao.resources.utils.search import SearchSystem

from .model import CampaignContactListModel

campaign_contact_list_config = SearchConfig(
    table=CampaignContactListModel,
    columns={
        'uuid': CampaignContactListModel.uuid,
    },
    default_sort='uuid',
)

campaign_contact_list_search = SearchSystem(campaign_contact_list_config)
