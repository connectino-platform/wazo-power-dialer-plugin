from marshmallow import fields
from wazo_confd.helpers.mallow import BaseSchema


class CampaignContactCallSchema(BaseSchema):
    uuid = fields.Str(dump_only=True)
    phone = fields.Str(dump_only=True)
    make_call = fields.DateTime(dump_only=True)
    call_answered = fields.DateTime(dump_only=True)
    playback_created = fields.DateTime(dump_only=True)
    playback_deleted = fields.DateTime(dump_only=True)
    call_deleted = fields.DateTime(dump_only=True)
    campaign_uuid = fields.Str(dump_only=True)
    contact_list_uuid = fields.Str(dump_only=True)
    contact_uuid = fields.Str(dump_only=True)
