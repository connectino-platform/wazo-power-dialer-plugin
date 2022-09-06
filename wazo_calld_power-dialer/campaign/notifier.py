from wazo_confd import bus, sysconfd


class SampleNotifier:
    def __init__(self, bus, sysconfd):
        self.bus = bus
        self.sysconfd = sysconfd

    def send_sysconfd_handlers(self):
        pass

    def created(self, sample):
        pass

    def edited(self, sample):
        pass

    def deleted(self, sample):
        pass


def build_sample_notifier():
    return SampleNotifier(bus, sysconfd)
