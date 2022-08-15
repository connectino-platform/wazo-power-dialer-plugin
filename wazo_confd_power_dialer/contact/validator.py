from wazo_confd.helpers.validator import Validator, ValidationGroup


class ContactValidator(Validator):
    def validate(self, model):
        return


def build_contact_validator():
    contact_validator = ContactValidator()
    return ValidationGroup(create=[contact_validator], edit=[contact_validator])
