from wazo_confd import bus, sysconfd


class ContactListNotifier:
    def __init__(self, bus, sysconfd):
        self.bus = bus
        self.sysconfd = sysconfd

    def send_sysconfd_handlers(self):
        pass

    def created(self, contact_list):
        pass

    def edited(self, contact_list):
        pass

    def deleted(self, contact_list):
        pass


def build_contact_list_notifier():
    return ContactListNotifier(bus, sysconfd)
