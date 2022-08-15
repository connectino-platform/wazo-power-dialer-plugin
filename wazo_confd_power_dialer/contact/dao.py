from xivo_dao.helpers.db_manager import daosession

from .persistor import ContactPersistor
from .search import contact_search


@daosession
def _persistor(session, tenant_uuids=None):
    return ContactPersistor(session, contact_search, tenant_uuids)


def search(tenant_uuids=None, **parameters):
    return _persistor(tenant_uuids).search(parameters)


def get(contact_uuid, tenant_uuids=None):
    return _persistor(tenant_uuids).get_by({'uuid': contact_uuid})


def get_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).get_by(criteria)


def find(contact_uuid, tenant_uuids=None):
    return _persistor(tenant_uuids).find_by({'uuid': contact_uuid})


def find_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).find_by(criteria)


def find_all_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).find_all_by(criteria)


def create(contact):
    return _persistor().create(contact)


def edit(contact):
    _persistor().edit(contact)


def delete(contact):
    _persistor().delete(contact)
