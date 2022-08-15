import logging

from flask import url_for, request
from wazo_confd.auth import required_acl
from wazo_confd.helpers.restful import ItemResource, ListResource

from .model import ContactListModel
from .schema import ContactListSchema

logger = logging.getLogger(__name__)


class ContactListListResource(ListResource):
    schema = ContactListSchema
    model = ContactListModel

    def build_headers(self, model):
        return {'Location': url_for('campaigns_contact_lists', uuid=model.uuid, _external=True)}

    @required_acl('confd.contact_lists.create')
    def post(self):
        return super().post()

    @required_acl('confd.contact_lists.read')
    def get(self):
        return super().get()


class ContactListItemResource(ItemResource):
    schema = ContactListSchema
    model = ContactListModel

    @required_acl('confd.contact_lists.read')
    def get(self, uuid):
        return super().get(uuid)

    @required_acl('confd.contact_lists.update')
    def put(self, uuid):
        return super().put(uuid)

    @required_acl('confd.contact_lists.delete')
    def delete(self, uuid):
        return super().delete(uuid)
