from marshmallow import fields
from wazo_confd.helpers.mallow import BaseSchema


class ContactSchema(BaseSchema):
    uuid = fields.Str(dump_only=True)
    tenant_uuid = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    family = fields.Str(required=True)
    phone = fields.Str(required=True)
    email = fields.Email(required=False)
    email2 = fields.Email(required=False)
    title = fields.Str(required=False)
    company = fields.Str(required=False)
    address = fields.Str(required=False)
    contact_lists = fields.Nested("ContactListSchema", exclude=("contacts", "campaigns"), many=True, dump_only=True)
