from xivo_dao.helpers.db_manager import daosession

from .persistor import CampaignContactListPersistor
from .search import campaign_contact_list_search


@daosession
def _persistor(session, tenant_uuids=None):
    return CampaignContactListPersistor(session, campaign_contact_list_search, tenant_uuids)


def search(tenant_uuids=None, **parameters):
    return _persistor(tenant_uuids).search(parameters)


def get(campaign_contact_list_uuid, tenant_uuids=None):
    return _persistor(tenant_uuids).get_by({'uuid': campaign_contact_list_uuid})


def get_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).get_by(criteria)


def find(campaign_contact_list_uuid, tenant_uuids=None):
    return _persistor(tenant_uuids).find_by({'uuid': campaign_contact_list_uuid})


def find_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).find_by(criteria)


def find_all_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).find_all_by(criteria)


def create(campaign_contact_list):
    return _persistor().create(campaign_contact_list)


def edit(campaign_contact_list):
    _persistor().edit(campaign_contact_list)


def delete(campaign_contact_list):
    _persistor().delete(campaign_contact_list)
