import threading, DataTransceiver, Server


class ClientThread(threading.Thread):
    def __init__(self, sock):
        threading.Thread.__init__(self)
        Server.ConnectionManager.user_list.append(self)
        print(Server.ConnectionManager.user_list[0])
        self.connectsocket = sock
        self.handler = DataTransceiver.DataTransceiver(self.connectsocket)
        

    def run(self):
        while True:
            if self.handler.handlePacket() == 0:
                break

        print("Disconnected a client from server.")
        Server.ConnectionManager.user_list.remove(self)
        self.connectsocket.close()
