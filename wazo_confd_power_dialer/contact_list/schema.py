from marshmallow import fields
from wazo_confd.helpers.mallow import BaseSchema


class ContactListSchema(BaseSchema):
    uuid = fields.Str(dump_only=True)
    tenant_uuid = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    contacts = fields.Nested("ContactSchema", exclude=("contact_lists",), many=True, dump_only=True)
