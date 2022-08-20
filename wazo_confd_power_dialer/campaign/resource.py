import logging

from flask import url_for, request
from wazo_confd.auth import required_acl
from wazo_confd.helpers.restful import ItemResource, ListResource

from .model import CampaignModel
from .schema import CampaignSchema

logger = logging.getLogger(__name__)


class CampaignListResource(ListResource):
    schema = CampaignSchema
    model = CampaignModel

    def build_headers(self, model):
        return {'Location': url_for('powerdialer_campaigns', uuid=model.uuid, _external=True)}

    @required_acl('confd.campaigns.create')
    def post(self):
        return super().post()

    @required_acl('confd.campaigns.read')
    def get(self):
        return super().get()


class CampaignItemResource(ItemResource):
    schema = CampaignSchema
    model = CampaignModel

    @required_acl('confd.campaigns.read')
    def get(self, uuid):
        return super().get(uuid)

    @required_acl('confd.campaigns.update')
    def put(self, uuid):
        return super().put(uuid)

    @required_acl('confd.campaigns.delete')
    def delete(self, uuid):
        return super().delete(uuid)
