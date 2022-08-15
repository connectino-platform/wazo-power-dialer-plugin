from wazo_confd.helpers.validator import Validator, ValidationGroup


class CampaignValidator(Validator):
    def validate(self, model):
        return


def build_campaign_validator():
    campaign_validator = CampaignValidator()
    return ValidationGroup(create=[campaign_validator], edit=[campaign_validator])
