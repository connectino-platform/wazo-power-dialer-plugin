from sqlalchemy import (
    Column,
    ForeignKey
)
from sqlalchemy import text
from xivo_dao.helpers.db_manager import UUIDAsString

from ..db import Base


class CampaignContactListModel(Base):
    __tablename__ = 'plugin_powerdialer_campaign_contact_list'

    uuid = Column(UUIDAsString(36), primary_key=True, server_default=text('uuid_generate_v4()'))
    campaign_uuid = Column(UUIDAsString(36), ForeignKey('plugin_powerdialer_campaign.uuid'), nullable=False)
    contact_list_uuid = Column(UUIDAsString(36), ForeignKey('plugin_powerdialer_contact_list.uuid'), nullable=False)
