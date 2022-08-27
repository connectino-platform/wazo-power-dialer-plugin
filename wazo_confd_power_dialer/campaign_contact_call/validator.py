from wazo_confd.helpers.validator import Validator, ValidationGroup


class CampaignContactCallValidator(Validator):
    def validate(self, model):
        return


def build_campaign_contact_call_validator():
    campaign_contact_call_validator = CampaignContactCallValidator()
    return ValidationGroup(create=[campaign_contact_call_validator], edit=[campaign_contact_call_validator])
