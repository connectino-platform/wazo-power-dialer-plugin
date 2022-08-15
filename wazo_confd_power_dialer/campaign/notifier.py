from wazo_confd import bus, sysconfd


class CampaignNotifier:
    def __init__(self, bus, sysconfd):
        self.bus = bus
        self.sysconfd = sysconfd

    def send_sysconfd_handlers(self):
        pass

    def created(self, campaign):
        pass

    def edited(self, campaign):
        pass

    def deleted(self, campaign):
        pass


def build_campaign_notifier():
    return CampaignNotifier(bus, sysconfd)
