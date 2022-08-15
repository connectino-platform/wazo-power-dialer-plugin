from sqlalchemy import (
    Column
)
from sqlalchemy import text
from sqlalchemy.types import (String, Boolean, Date, Time, Integer)
from xivo_dao.helpers.db_manager import UUIDAsString

from ..db import Base


class CampaignModel(Base):
    __tablename__ = 'plugin_powerdialer_campaign'

    uuid = Column(UUIDAsString(36), primary_key=True, server_default=text('uuid_generate_v4()'))
    tenant_uuid = Column(UUIDAsString(36), nullable=False)
    name = Column(String(128), nullable=False)
    status = Column(String(128), nullable=False)
    schedule_start_date = Column(Date, nullable=True)
    schedule_start_time = Column(Time, nullable=True)
    answer_wait_time = Column(Integer, nullable=False)
    after_call_dialing_auto = Column(Boolean, nullable=False)
    after_call_time = Column(Integer, nullable=False)
    is_recording = Column(Boolean, nullable=False)
    attempts = Column(Integer, nullable=False)
    attempts_interval = Column(Integer, nullable=False)
