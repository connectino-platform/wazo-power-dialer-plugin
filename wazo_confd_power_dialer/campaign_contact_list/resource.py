import logging

from flask import url_for, request
from wazo_confd.auth import required_acl
from wazo_confd.helpers.restful import ListResource

from .model import CampaignContactListModel
from .schema import CampaignContactListSchema

logger = logging.getLogger(__name__)


class CampaignContactListListResource(ListResource):
    schema = CampaignContactListSchema
    model = CampaignContactListModel

    def build_headers(self, model):
        return {'Location': url_for(
            'powerdialer_campaigns_contact_lists',
            contact_list_uuid=model.contact_list_uuid,
            campaign_uuid=model.campaign_uuid,
            _external=True
        )}

    @required_acl('confd.powerdialer.campaign_contact_lists.create')
    def post(self, campaign_uuid, contact_list_uuid):
        form = self.schema().load(request.get_json())
        form = self.add_tenant_to_form(form)
        model = self.model(**form)
        model.contact_list_uuid = contact_list_uuid
        model.campaign_uuid = campaign_uuid

        model = self.service.create(model)
        return self.schema().dump(model), 201, self.build_headers(model)

    @required_acl('confd.powerdialer.campaign_contact_lists.delete')
    def delete(self, contact_list_uuid, campaign_uuid):
        models = self.service.search({"contact_list_uuid": contact_list_uuid, "campaign_uuid": campaign_uuid})
        for model in models.items:
            self.service.delete(model)
        return '', 204
