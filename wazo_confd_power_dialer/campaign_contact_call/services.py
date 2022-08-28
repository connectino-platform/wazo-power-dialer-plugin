from wazo_confd.helpers.resource import CRUDService

from . import dao
from .notifier import build_campaign_contact_call_notifier
from .validator import build_campaign_contact_call_validator


def build_campaign_contact_call_service():
    return CampaignContactCallService(dao, build_campaign_contact_call_validator(),
                                      build_campaign_contact_call_notifier())


class CampaignContactCallService(CRUDService):

    def __init__(self, dao, validator, notifier, extra_parameters=None):
        super().__init__(dao, validator, notifier, extra_parameters)

    def get_last_cantact_call(self, campaign_uuid):
        return self.dao.get_last_cantact_call(campaign_uuid)
