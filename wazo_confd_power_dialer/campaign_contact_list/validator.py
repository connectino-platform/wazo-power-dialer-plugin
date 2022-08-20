from wazo_confd.helpers.validator import Validator, ValidationGroup


class CampaignContactListValidator(Validator):
    def validate(self, model):
        return


def build_campaign_contact_list_validator():
    campaign_contact_list_validator = CampaignContactListValidator()
    return ValidationGroup(create=[campaign_contact_list_validator], edit=[campaign_contact_list_validator])
