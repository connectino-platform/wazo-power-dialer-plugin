import logging

from flask import url_for
from xivo.tenant_flask_helpers import Tenant
from wazo_confd.auth import required_acl
from wazo_confd.helpers.restful import ItemResource, ListResource
from wazo_confd.helpers.restful import ConfdResource

from . import csvparse
from .model import ContactModel
from .schema import ContactSchema

logger = logging.getLogger(__name__)


class ContactListResource(ListResource):
    schema = ContactSchema
    model = ContactModel

    def build_headers(self, model):
        return {'Location': url_for('powerdialer_contacts', uuid=model.uuid, _external=True)}

    @required_acl('confd.contacts.create')
    def post(self):
        return super().post()

    @required_acl('confd.contacts.read')
    def get(self):
        return super().get()


class ContactItemResource(ItemResource):
    schema = ContactSchema
    model = ContactModel

    @required_acl('confd.powerdialer.contacts.{uuid}.read')
    def get(self, uuid):
        return super().get(uuid)

    @required_acl('confd.powerdialer.contacts.{uuid}.update')
    def put(self, uuid):
        return super().put(uuid)

    @required_acl('confd.powerdialer.contacts.{uuid}.delete')
    def delete(self, uuid):
        return super().delete(uuid)


class ContactImportResource(ConfdResource):
    schema = ContactSchema

    def __init__(self, service):
        self.service = service

    @required_acl('confd.powerdialer.contacts.import')
    def post(self, contact_list_uuid):
        tenant = Tenant.autodetect()

        parser = csvparse.parse()
        entries, errors = self.service.import_rows(parser, tenant.uuid, contact_list_uuid)

        return {'created': self.schema().dump(entries, many=True), 'errors': errors}, 201
