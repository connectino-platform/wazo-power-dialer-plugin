from marshmallow import fields
from marshmallow.validate import OneOf
from wazo_confd.helpers.mallow import BaseSchema


class CampaignSchema(BaseSchema):
    uuid = fields.Str(dump_only=True)
    tenant_uuid = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    status = fields.String(validate=OneOf(['active', 'inactive']), allow_none=False)
    schedule_start_date = fields.Date()
    schedule_start_time = fields.Time()
    answer_wait_time = fields.Integer(required=False, default=60)
    after_call_dialing_auto = fields.Boolean(required=False, default=True)
    after_call_time = fields.Integer(required=False, default=0)
    is_recording = fields.Boolean(required=False, default=False)
    attempts = fields.Integer(required=False, default=1)
    attempts_interval = fields.Integer(required=False, default=10)
