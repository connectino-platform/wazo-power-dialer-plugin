from sqlalchemy import (
    Column
)
from sqlalchemy import text
from sqlalchemy.orm import relationship
from sqlalchemy.types import String
from xivo_dao.helpers.db_manager import UUIDAsString

from ..db import Base


class ContactModel(Base):
    __tablename__ = 'plugin_powerdialer_contact'

    uuid = Column(UUIDAsString(36), primary_key=True, server_default=text('uuid_generate_v4()'))
    tenant_uuid = Column(UUIDAsString(36), nullable=False)
    name = Column(String(128), nullable=False)
    family = Column(String(128), nullable=False)
    phone = Column(String(128), nullable=False)
    email = Column(String(128), nullable=True)
    email2 = Column(String(128), nullable=True)
    title = Column(String(128), nullable=True)
    company = Column(String(128), nullable=True)
    address = Column(String(512), nullable=True)
    contact_lists = relationship(
        'ContactListModel',
        secondary='plugin_powerdialer_contact_contact_list',
    )
