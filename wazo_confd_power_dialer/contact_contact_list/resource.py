import logging

from flask import url_for, request
from wazo_confd.auth import required_acl
from wazo_confd.helpers.restful import ItemResource, ListResource

from .model import ContactContactListModel
from .schema import ContactContactListSchema

logger = logging.getLogger(__name__)


class ContactContactListListResource(ListResource):
    schema = ContactContactListSchema
    model = ContactContactListModel

    def build_headers(self, model):
        return {'Location': url_for(
            'campaigns_contact_contact_lists',
            contact_list_uuid=model.contact_list_uuid,
            contact_uuid=model.contact_uuid,
            _external=True
        )}

    @required_acl('confd.contact_contact_lists.create')
    def post(self, contact_list_uuid, contact_uuid):
        form = self.schema().load(request.get_json())
        form = self.add_tenant_to_form(form)
        model = self.model(**form)
        model.contact_list_uuid = contact_list_uuid
        model.contact_uuid = contact_uuid
        model = self.service.create(model)
        return self.schema().dump(model), 201, self.build_headers(model)

    # @required_acl('confd.contact_contact_lists.read')
    # def get(self):
    #     return super().get()

    @required_acl('confd.contact_contact_lists.delete')
    def delete(self, contact_list_uuid, contact_uuid):
        models = self.service.search({"contact_list_uuid": contact_list_uuid, "contact_uuid": contact_uuid})
        logger.info(models)
        for model in models.items:
            self.service.delete(model)
        return '', 204


# class ContactContactListItemResource(ItemResource):
#     schema = ContactContactListSchema
#     model = ContactContactListModel
#
#     @required_acl('confd.contact_contact_lists.read')
#     def get(self, uuid):
#         return super().get(uuid)
#
#     @required_acl('confd.contact_contact_lists.update')
#     def put(self, uuid):
#         return super().put(uuid)
#
#     @required_acl('confd.contact_contact_lists.delete')
#     def delete(self, uuid):
#         return super().delete(uuid)
