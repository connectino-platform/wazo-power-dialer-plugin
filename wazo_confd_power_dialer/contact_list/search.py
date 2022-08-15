from xivo_dao.resources.utils.search import SearchConfig
from xivo_dao.resources.utils.search import SearchSystem

from .model import ContactListModel

contact_list_config = SearchConfig(
    table=ContactListModel,
    columns={
        'uuid': ContactListModel.uuid,
        'name': ContactListModel.name,
    },
    default_sort='name',
)

contact_list_search = SearchSystem(contact_list_config)
