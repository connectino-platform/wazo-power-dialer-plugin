from wazo_confd.helpers.resource import CRUDService

from . import dao
from .notifier import build_campaign_notifier
from .validator import build_campaign_validator


def build_campaign_service():
    return CRUDService(dao, build_campaign_validator(), build_campaign_notifier())
