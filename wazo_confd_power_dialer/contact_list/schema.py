from marshmallow import fields
from wazo_confd.helpers.mallow import BaseSchema


class ContactListSchema(BaseSchema):
    uuid = fields.Str(dump_only=True)
    tenant_uuid = fields.Str(dump_only=True)
    name = fields.Str(required=True)
