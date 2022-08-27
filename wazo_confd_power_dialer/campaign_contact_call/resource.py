import logging

from flask import url_for, request
from wazo_confd.auth import required_acl
from wazo_confd.helpers.restful import ItemResource, ListResource

from .model import CampaignContactCallModel
from .schema import CampaignContactCallSchema

logger = logging.getLogger(__name__)


class CampaignContactCallListResource(ListResource):
    schema = CampaignContactCallSchema
    model = CampaignContactCallModel

    def build_headers(self, model):
        return {'Location': url_for('powerdialer_campaign_contact_calls', uuid=model.uuid, _external=True)}

    @required_acl('confd.powerdialer.campaign_contact_calls.read')
    def get(self):
        return super().get()


class CampaignContactCallItemResource(ItemResource):
    schema = CampaignContactCallSchema
    model = CampaignContactCallModel

    @required_acl('confd.powerdialer.campaign_contact_calls.{uuid}.read')
    def get(self, uuid):
        return super().get(uuid)

