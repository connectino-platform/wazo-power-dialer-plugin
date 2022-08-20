import logging

from flask import url_for, request
from wazo_confd.auth import required_acl
from wazo_confd.helpers.restful import ItemResource, ListResource

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

    @required_acl('confd.contacts.read')
    def get(self, uuid):
        return super().get(uuid)

    @required_acl('confd.contacts.update')
    def put(self, uuid):
        return super().put(uuid)

    @required_acl('confd.contacts.delete')
    def delete(self, uuid):
        return super().delete(uuid)
