from xivo_dao.helpers.db_manager import daosession

from .persistor import CampaignContactCallPersistor
from .search import campaign_contact_call_search


@daosession
def _persistor(session, tenant_uuids=None):
    return CampaignContactCallPersistor(session, campaign_contact_call_search, tenant_uuids)


def search(tenant_uuids=None, **parameters):
    return _persistor(tenant_uuids).search(parameters)


def get(campaign_contact_call_uuid, tenant_uuids=None):
    return _persistor(tenant_uuids).get_by({'uuid': campaign_contact_call_uuid})


def get_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).get_by(criteria)


def find(campaign_contact_call_uuid, tenant_uuids=None):
    return _persistor(tenant_uuids).find_by({'uuid': campaign_contact_call_uuid})


def find_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).find_by(criteria)


def find_all_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).find_all_by(criteria)


def create(campaign_contact_call):
    return _persistor().create(campaign_contact_call)


def edit(campaign_contact_call):
    _persistor().edit(campaign_contact_call)


def delete(campaign_contact_call):
    _persistor().delete(campaign_contact_call)
