from sqlalchemy import (
    Column
)
from sqlalchemy import text
from sqlalchemy.orm import relationship
from sqlalchemy.types import String
from xivo_dao.helpers.db_manager import UUIDAsString

from ..db import Base


class ContactListModel(Base):
    __tablename__ = 'plugin_powerdialer_contact_list'

    uuid = Column(UUIDAsString(36), primary_key=True, server_default=text('uuid_generate_v4()'))
    tenant_uuid = Column(UUIDAsString(36), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(512), nullable=True)
    contacts = relationship(
        'ContactModel',
        secondary='plugin_powerdialer_contact_contact_list'
    )
    campaigns = relationship(
        'CampaignModel',
        secondary='plugin_powerdialer_campaign_contact_list'
    )
