import logging

from flask import url_for
from wazo_confd.auth import required_acl
from wazo_confd.helpers.restful import ItemResource, ListResource, ConfdResource
from wazo_confd.plugins.application.schema import ApplicationSchema
from xivo.tenant_flask_helpers import Tenant
from .model import CampaignModel
from .schema import CampaignSchema

logger = logging.getLogger(__name__)


class CampaignListResource(ListResource):
    schema = CampaignSchema
    model = CampaignModel

    def build_headers(self, model):
        return {'Location': url_for('powerdialer_campaigns', uuid=model.uuid, _external=True)}

    @required_acl('confd.powerdialer.campaigns.create')
    def post(self):
        return super().post()

    @required_acl('confd.powerdialer.campaigns.read')
    def get(self):
        return super().get()


class CampaignItemResource(ItemResource):
    schema = CampaignSchema
    model = CampaignModel

    @required_acl('confd.powerdialer.campaigns.{uuid}.read')
    def get(self, uuid):
        return super().get(uuid)

    @required_acl('confd.powerdialer.campaigns.{uuid}.update')
    def put(self, uuid):
        return super().put(uuid)

    @required_acl('confd.powerdialer.campaigns.{uuid}.delete')
    def delete(self, uuid):
        return super().delete(uuid)


class CampaignRunnerResource(ConfdResource):
    def __init__(self, service):
        self.service = service

    def post(self, uuid):
        application = self.service.start(uuid)
        return application
