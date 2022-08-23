from wazo_confd.helpers.resource import CRUDService

from . import dao
from .notifier import build_contact_contact_list_notifier
from .validator import build_contact_contact_list_validator


def build_contact_contact_list_service():
    return ContactContactListService(dao, build_contact_contact_list_validator(), build_contact_contact_list_notifier())


class ContactContactListService(CRUDService):
    def create(self, resource):
        already_associated = self.search({
            "contact_list_uuid": resource.contact_list_uuid,
            "contact_uuid": resource.contact_uuid
        })
        if already_associated.total:
            created_resource = already_associated.items[0]
        else:
            created_resource = super().create(resource)
        return created_resource
