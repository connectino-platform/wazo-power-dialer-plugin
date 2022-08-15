from wazo_confd import bus, sysconfd


class ContactContactListNotifier:
    def __init__(self, bus, sysconfd):
        self.bus = bus
        self.sysconfd = sysconfd

    def send_sysconfd_handlers(self):
        pass

    def created(self, contact_contact_list):
        pass

    def edited(self, contact_contact_list):
        pass

    def deleted(self, contact_contact_list):
        pass


def build_contact_contact_list_notifier():
    return ContactContactListNotifier(bus, sysconfd)
