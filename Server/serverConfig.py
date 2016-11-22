class ServerConfig(object):
    def __init__(self, filename):
        self.setting_file = filename
        self.CONFIG_MAP = []

    def load(self):
        with open(self.setting_file, 'r') as f:
            for v in f:
                self.CONFIG_MAP.append(v.replace('\n', ''))
        return self.CONFIG_MAP
