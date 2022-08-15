from xivo_dao.helpers.persistor import BasePersistor
from xivo_dao.resources.utils.search import CriteriaBuilderMixin

from .model import CampaignModel


class CampaignPersistor(CriteriaBuilderMixin, BasePersistor):
    _search_table = CampaignModel

    def __init__(self, session, campaign_search, tenant_uuids=None):
        self.session = session
        self.search_system = campaign_search
        self.tenant_uuids = tenant_uuids

    def _find_query(self, criteria):
        query = self.session.query(CampaignModel)
        # query = self._filter_tenant_uuid(query)
        return self.build_criteria(query, criteria)

    def _search_query(self):
        return self.session.query(self.search_system.config.table)
