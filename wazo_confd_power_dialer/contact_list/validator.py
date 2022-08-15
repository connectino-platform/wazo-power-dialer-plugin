from wazo_confd.helpers.validator import Validator, ValidationGroup


class ContactListValidator(Validator):
    def validate(self, model):
        return


def build_contact_list_validator():
    contact_list_validator = ContactListValidator()
    return ValidationGroup(create=[contact_list_validator], edit=[contact_list_validator])
