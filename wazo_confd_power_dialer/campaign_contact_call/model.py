from sqlalchemy import (
    Column, ForeignKey
)
from sqlalchemy import text
from sqlalchemy.types import String, DateTime
from xivo_dao.helpers.db_manager import UUIDAsString

from ..db import Base


class CampaignContactCallModel(Base):
    __tablename__ = 'plugin_powerdialer_campaign_contact_call'

    uuid = Column(UUIDAsString(36), primary_key=True, server_default=text('uuid_generate_v4()'))
    phone = Column(String(128), nullable=False)
    make_call = Column(DateTime, nullable=True)
    call_answered = Column(DateTime, nullable=True)
    playback_created = Column(DateTime, nullable=True)
    playback_deleted = Column(DateTime, nullable=True)
    call_deleted = Column(DateTime, nullable=True)
    campaign_uuid = Column(UUIDAsString(36), ForeignKey('plugin_powerdialer_campaign.uuid'), nullable=True)
    contact_list_uuid = Column(UUIDAsString(36), ForeignKey('plugin_powerdialer_contact_list.uuid'), nullable=True)
    contact_uuid = Column(UUIDAsString(36), ForeignKey('plugin_powerdialer_contact.uuid'), nullable=True)
