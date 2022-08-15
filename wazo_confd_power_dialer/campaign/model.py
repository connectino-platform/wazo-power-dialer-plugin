from sqlalchemy import (
    Column
)
from sqlalchemy import text
from sqlalchemy.types import String
from xivo_dao.helpers.db_manager import UUIDAsString

from ..db import Base


class CampaignModel(Base):
    __tablename__ = 'plugin_campaign'

    uuid = Column(UUIDAsString(36), primary_key=True, server_default=text('uuid_generate_v4()'))
    name = Column(String(128), nullable=False)
