from wazo_confd.helpers.validator import Validator, ValidationGroup


class ContactContactListValidator(Validator):
    def validate(self, model):
        return


def build_contact_contact_list_validator():
    contact_contact_list_validator = ContactContactListValidator()
    return ValidationGroup(create=[contact_contact_list_validator], edit=[contact_contact_list_validator])
