from wazo_confd.helpers.resource import CRUDService

from . import dao
from .notifier import build_campaign_contact_list_notifier
from .validator import build_campaign_contact_list_validator


def build_campaign_contact_list_service():
    return CampaignContactListService(dao, build_campaign_contact_list_validator(),
                                      build_campaign_contact_list_notifier())


class CampaignContactListService(CRUDService):
    def create(self, resource):
        already_associated = self.search({
            "campaign_uuid": resource.campaign_uuid,
            "contact_list_uuid": resource.contact_list_uuid
        })
        if already_associated.total:
            created_resource = already_associated.items[0]
        else:
            created_resource = super().create(resource)
        return created_resource
