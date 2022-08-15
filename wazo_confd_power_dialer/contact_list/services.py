from wazo_confd.helpers.resource import CRUDService

from . import dao
from .notifier import build_contact_list_notifier
from .validator import build_contact_list_validator


def build_contact_list_service():
    return CRUDService(dao, build_contact_list_validator(), build_contact_list_notifier())
