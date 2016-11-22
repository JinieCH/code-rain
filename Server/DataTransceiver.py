import json,Packet, Server

# For purpose to both transmit and receive.
class DataTransceiver(object):
    def __init__(self, sock):
        self.max_bytes = 1024
        self.socket = sock

    def send_data(self, data):
        self.socket.send(json.dumps(data.packet).encode())
        
    def broadcast_data(self, data):
        for instance in Server.ConnectionManager.user_list:
            instance.connectsocket.send(json.dumps(data.packet).encode())

    def recv_data(self):
        raw_string = self.socket.recv(self.max_bytes).decode()
        if not raw_string:
            return Packet(-1, 'None')
        parsed_json = json.loads(raw_string)
        return Packet.Packet(parsed_json['code'], parsed_json['payload'])

    def handlePacket(self):
        packet = self.recv_data()
        code = packet.get_code()
        if code == -1: # error
            pass
        elif code == 0: # login
            if Server.ConnectionManager.db_handler.read('UserList', 'id', 'password', packet.get_payload()):
                p = Packet.Packet(1, 'success to login')
                self.send_data(p)
            else:
                p = Packet.Packet(0, 'failed to login')
                self.send_data(p)
        elif code == 1: # logout
            return 0
        elif code == 2: # sign in
            Server.databse.insert('UserList', 'id', 'password', packet.get_payload())
        elif code == 3: # game start
            pass
