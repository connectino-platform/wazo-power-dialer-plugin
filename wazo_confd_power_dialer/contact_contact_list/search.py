from xivo_dao.resources.utils.search import SearchConfig
from xivo_dao.resources.utils.search import SearchSystem

from .model import ContactContactListModel

contact_contact_list_config = SearchConfig(
    table=ContactContactListModel,
    columns={
        'uuid': ContactContactListModel.uuid,
        'name': ContactContactListModel.name,
    },
    default_sort='name',
)

contact_contact_list_search = SearchSystem(contact_contact_list_config)
