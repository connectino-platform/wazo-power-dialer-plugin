from marshmallow import fields
from wazo_confd.helpers.mallow import BaseSchema


class CampaignContactListSchema(BaseSchema):
    uuid = fields.Str(dump_only=True)
    campaign_uuid = fields.String(dump_only=True)
    contact_list_uuid = fields.String(dump_only=True)
