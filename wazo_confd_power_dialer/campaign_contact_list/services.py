from wazo_confd.helpers.resource import CRUDService

from . import dao
from .notifier import build_campaign_contact_list_notifier
from .validator import build_campaign_contact_list_validator


def build_campaign_contact_list_service():
    return CRUDService(dao, build_campaign_contact_list_validator(), build_campaign_contact_list_notifier())
