from xivo_dao.resources.utils.search import SearchConfig
from xivo_dao.resources.utils.search import SearchSystem

from .model import ContactModel

contact_config = SearchConfig(
    table=ContactModel,
    columns={
        'uuid': ContactModel.uuid,
        'name': ContactModel.name,
    },
    default_sort='name',
)

contact_search = SearchSystem(contact_config)
