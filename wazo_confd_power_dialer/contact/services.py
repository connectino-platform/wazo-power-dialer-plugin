from wazo_confd.helpers.resource import CRUDService

from . import dao
from .model import ContactModel
from .notifier import build_contact_notifier
from .schema import ContactSchema
from .validator import build_contact_validator
import logging
from marshmallow import ValidationError
from xivo_dao.helpers.exception import ServiceError

from ..contact_contact_list.model import ContactContactListModel
from ..contact_contact_list.services import build_contact_contact_list_service

logger = logging.getLogger(__name__)


def build_contact_service():
    return ContactService(build_contact_contact_list_service(), dao, build_contact_validator(),
                          build_contact_notifier())


class ContactService(CRUDService):
    def __init__(self, contact_contact_list_service, dao, validator, notifier, extra_parameters=None):
        self.contact_contact_list_service = contact_contact_list_service
        super().__init__(dao, validator, notifier, extra_parameters)

    def create(self, resource):
        already_associated = self.search({"phone": resource.phone, "tenant_uuid": resource.tenant_uuid}, )
        if already_associated.total:
            raise ServiceError(f"Contact with phone {resource.phone} already exist for tenant {resource.tenant_uuid}",
                               already_associated.items[0])
        else:
            created_resource = super().create(resource)
        return created_resource

    def import_rows(self, parser, tenant_uuid, contact_list_uuid):
        created = []
        errors = []

        for row in parser:
            if not row:
                continue

            try:
                form = ContactSchema(handle_error=False).load(row.parse())
                form['tenant_uuid'] = tenant_uuid
                contact = self.create(ContactModel(**form))
                contact_contact_list = ContactContactListModel()
                contact_contact_list.contact_list_uuid = contact_list_uuid
                contact_contact_list.contact_uuid = contact.uuid
                self.contact_contact_list_service.create(contact_contact_list)
                created.append(contact)

            except (ServiceError, ValidationError) as e:
                logger.warning("Error importing CSV row %s: %s", row.position, e)
                errors.append(row.format_error(e))

        return created, errors
