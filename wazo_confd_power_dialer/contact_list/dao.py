from xivo_dao.helpers.db_manager import daosession

from .persistor import ContactListPersistor
from .search import contact_list_search


@daosession
def _persistor(session, tenant_uuids=None):
    return ContactListPersistor(session, contact_list_search, tenant_uuids)


def search(tenant_uuids=None, **parameters):
    return _persistor(tenant_uuids).search(parameters)


def get(contact_list_uuid, tenant_uuids=None):
    return _persistor(tenant_uuids).get_by({'uuid': contact_list_uuid})


def get_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).get_by(criteria)


def find(contact_list_uuid, tenant_uuids=None):
    return _persistor(tenant_uuids).find_by({'uuid': contact_list_uuid})


def find_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).find_by(criteria)


def find_all_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).find_all_by(criteria)


def create(contact_list):
    return _persistor().create(contact_list)


def edit(contact_list):
    _persistor().edit(contact_list)


def delete(contact_list):
    _persistor().delete(contact_list)
