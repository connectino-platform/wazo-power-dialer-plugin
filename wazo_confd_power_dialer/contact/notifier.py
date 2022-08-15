from wazo_confd import bus, sysconfd


class ContactNotifier:
    def __init__(self, bus, sysconfd):
        self.bus = bus
        self.sysconfd = sysconfd

    def send_sysconfd_handlers(self):
        pass

    def created(self, contact):
        pass

    def edited(self, contact):
        pass

    def deleted(self, contact):
        pass


def build_contact_notifier():
    return ContactNotifier(bus, sysconfd)
