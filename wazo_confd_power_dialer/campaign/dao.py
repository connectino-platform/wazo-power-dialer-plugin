from xivo_dao.helpers.db_manager import daosession

from .persistor import CampaignPersistor
from .search import campaign_search


@daosession
def _persistor(session, tenant_uuids=None):
    return CampaignPersistor(session, campaign_search, tenant_uuids)


def search(tenant_uuids=None, **parameters):
    return _persistor(tenant_uuids).search(parameters)


def get(campaign_uuid, tenant_uuids=None):
    return _persistor(tenant_uuids).get_by({'uuid': campaign_uuid})


def get_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).get_by(criteria)


def find(campaign_uuid, tenant_uuids=None):
    return _persistor(tenant_uuids).find_by({'uuid': campaign_uuid})


def find_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).find_by(criteria)


def find_all_by(tenant_uuids=None, **criteria):
    return _persistor(tenant_uuids).find_all_by(criteria)


def create(campaign):
    return _persistor().create(campaign)


def edit(campaign):
    _persistor().edit(campaign)


def delete(campaign):
    _persistor().delete(campaign)
