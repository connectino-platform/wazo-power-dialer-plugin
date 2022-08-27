from wazo_confd.helpers.resource import CRUDService

from . import dao
from .notifier import build_campaign_contact_call_notifier
from .validator import build_campaign_contact_call_validator


def build_campaign_contact_call_service():
    return CRUDService(dao, build_campaign_contact_call_validator(), build_campaign_contact_call_notifier())
