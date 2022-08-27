from wazo_confd import bus, sysconfd


class CampaignContactCallNotifier:
    def __init__(self, bus, sysconfd):
        self.bus = bus
        self.sysconfd = sysconfd

    def send_sysconfd_handlers(self):
        pass

    def created(self, campaign_contact_call):
        pass

    def edited(self, campaign_contact_call):
        pass

    def deleted(self, campaign_contact_call):
        pass


def build_campaign_contact_call_notifier():
    return CampaignContactCallNotifier(bus, sysconfd)
