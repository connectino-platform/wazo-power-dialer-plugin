import logging

from flask import url_for
from wazo_confd.auth import required_acl
from wazo_confd.helpers.restful import ItemResource, ListResource, ConfdResource
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


class CampaignStartResource(ConfdResource):
    schema = CampaignSchema

    def __init__(self, service):
        self.service = service

    @required_acl('confd.powerdialer.campaigns.{uuid}.start')
    def put(self, uuid):
        model = self.service.start(uuid)
        return self.schema().dump(model)


class CampaignPauseResource(ConfdResource):
    schema = CampaignSchema

    def __init__(self, service):
        self.service = service

    @required_acl('confd.powerdialer.campaigns.{uuid}.pause')
    def put(self, uuid):
        model = self.service.pause(uuid)
        return self.schema().dump(model)


class CampaignStopResource(ConfdResource):
    schema = CampaignSchema

    def __init__(self, service):
        self.service = service

    @required_acl('confd.powerdialer.campaigns.{uuid}.stop')
    def put(self, uuid):
        model = self.service.stop(uuid)
        return self.schema().dump(model)


class CampaignResumeResource(ConfdResource):
    schema = CampaignSchema

    def __init__(self, service):
        self.service = service

    @required_acl('confd.powerdialer.campaigns.{uuid}.resume')
    def put(self, uuid):
        model = self.service.resume(uuid)
        return self.schema().dump(model)
