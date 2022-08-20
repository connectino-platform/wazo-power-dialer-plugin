from wazo_confd import bus, sysconfd


class CampaignContactListNotifier:
    def __init__(self, bus, sysconfd):
        self.bus = bus
        self.sysconfd = sysconfd

    def send_sysconfd_handlers(self):
        pass

    def created(self, campaign_contact_list):
        pass

    def edited(self, campaign_contact_list):
        pass

    def deleted(self, campaign_contact_list):
        pass


def build_campaign_contact_list_notifier():
    return CampaignContactListNotifier(bus, sysconfd)
