from sqlalchemy import (
    Column
)
from sqlalchemy import text, Table, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import String
from xivo_dao.helpers.db_manager import UUIDAsString

from ..contact.model import ContactModel
from ..contact_contact_list.model import ContactContactListModel
from ..db import Base


class ContactListModel(Base):
    __tablename__ = 'plugin_powerdialer_contact_list'

    # association_table = Table(
    #     ContactContactListModel,
    #     Base.metadata,
    #     Column("contact_uuid", ForeignKey("ContactModel.uuid"), primary_key=True),
    #     Column("contact_list_uuid", ForeignKey("ContactListModel.uuid"), primary_key=True),
    # )

    uuid = Column(UUIDAsString(36), primary_key=True, server_default=text('uuid_generate_v4()'))
    tenant_uuid = Column(UUIDAsString(36), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(512), nullable=True)
    contacts = relationship(ContactModel, secondary=ContactContactListModel)
