from marshmallow import fields
from wazo_confd.helpers.mallow import BaseSchema


class CampaignSchema(BaseSchema):
    uuid = fields.Str(dump_only=True)
    name = fields.Str(required=True)
