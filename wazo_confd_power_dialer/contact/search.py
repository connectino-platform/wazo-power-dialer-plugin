from xivo_dao.resources.utils.search import SearchConfig
from xivo_dao.resources.utils.search import SearchSystem

from .model import ContactModel

contact_config = SearchConfig(
    table=ContactModel,
    columns={
        'uuid': ContactModel.uuid,
        'name': ContactModel.name,
        "phone": ContactModel.phone,
        "tenant_uuid": ContactModel.tenant_uuid,
    },
    default_sort='name',
)

contact_search = SearchSystem(contact_config)
