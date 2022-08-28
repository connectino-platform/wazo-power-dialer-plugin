import logging

from sqlalchemy import and_
from sqlalchemy.dialects import postgresql
from xivo_dao.helpers.persistor import BasePersistor
from xivo_dao.resources.utils.search import CriteriaBuilderMixin

from .model import CampaignContactCallModel

logger = logging.getLogger(__name__)


class CampaignContactCallPersistor(CriteriaBuilderMixin, BasePersistor):
    _search_table = CampaignContactCallModel

    def __init__(self, session, campaign_contact_call_search, tenant_uuids=None):
        self.session = session
        self.search_system = campaign_contact_call_search
        self.tenant_uuids = tenant_uuids

    def _find_query(self, criteria):
        query = self.session.query(CampaignContactCallModel)
        # query = self._filter_tenant_uuid(query)
        return self.build_criteria(query, criteria)

    def _search_query(self):
        return self.session.query(self.search_system.config.table)

    def get_last_cantact_call(self, campaign_uuid):
        query = self.session.query(CampaignContactCallModel).filter(
            and_(CampaignContactCallModel.campaign_uuid == campaign_uuid,
                 CampaignContactCallModel.make_call.isnot(None))
        ).order_by(CampaignContactCallModel.make_call.desc())
        logger.info(str(query))
        return query.first()
