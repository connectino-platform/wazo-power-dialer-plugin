from wazo_confd.helpers.resource import CRUDService

from . import dao
from .notifier import build_contact_notifier
from .validator import build_contact_validator


def build_contact_service():
    return CRUDService(dao, build_contact_validator(), build_contact_notifier())
