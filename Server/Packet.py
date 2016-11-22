class Packet(object):
    def __init__(self, code, payload):
        self.packet = {'code': -1, 'payload': []}
        self.set_code(code)
        self.set_payload(payload)

    def set_code(self, code):
        self.packet['code'] = code

    def set_payload(self, data):
        self.packet['payload'] = data

    def get_code(self):
        return self.packet['code']

    def get_payload(self):
        return self.packet['payload']
