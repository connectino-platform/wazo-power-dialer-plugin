from marshmallow import fields
from wazo_confd.helpers.mallow import BaseSchema

from wazo_confd_power_dialer.contact.schema import ContactSchema


class ContactListSchema(BaseSchema):
    uuid = fields.Str(dump_only=True)
    tenant_uuid = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    contacts = fields.Nested(ContactSchema, many=True, dump_only=True)
