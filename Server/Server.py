from socket import *
import threading, json, DB, serverConfig, thread, wordManager

class ConnectionManager(object):
    db_handler = DB.DBConnector()
    user_list = []

    def __init__(self):
        self.CONFIG_MAP = serverConfig.ServerConfig('ServerInfo.txt').load()
        self.serversocket = socket(AF_INET, SOCK_STREAM)
        print (self.CONFIG_MAP[0])
        self.serversocket.bind((self.CONFIG_MAP[0], int(self.CONFIG_MAP[1])))
        self.serversocket.listen(int(self.CONFIG_MAP[2]))
        ConnectionManager.db_handler.open(self.CONFIG_MAP[3])
        ConnectionManager.db_handler.createTable('UserList', 'id', 'TEXT', 'password', 'TEXT')
        ConnectionManager.db_handler.createTable('Clang', 'fname', 'TEXT', 'desc', 'TEXT')
        ConnectionManager.db_handler.createTable('Javalang', 'fname', 'TEXT', 'desc', 'TEXT')
        ConnectionManager.db_handler.createTable('Pylang', 'fname', 'TEXT', 'desc', 'TEXT')

        #with open('c_function.txt', 'r') as f:
        #    for line in f:
        #        ConnectionManager.db_handler.insert('Clang', 'fname', 'desc', [line.replace('\n', ''), 'None'])
        #with open('java_function.txt', 'r') as f:
        #    for line in f:
        #        ConnectionManager.db_handler.insert('Javalang', 'fname', 'desc', [line.replace('\n', ''), 'None'])
        #with open('python_function.txt', 'r') as f:
        #    for line in f:
        #        ConnectionManager.db_handler.insert('Pylang', 'fname', 'desc', [line.replace('\n', ''), 'None'])

        ConnectionManager.db_handler.insert('UserList', 'id', 'password', ['admin', '111'])
        print("The server starting and waiting from clients...")

    def start(self):
        while True:
            connect, addr = self.serversocket.accept()
            print("Connected with " + addr[0] + " : " + str(addr[1]))
            t = thread.ClientThread(connect) # make a new thread corresponding with its socket.
            t.start() # run a thread.

        self.disconnect()
        
    def disconnect(self):
        self.serversocket.close()
        ConnectionManager.db_handler.close()


class Word(object):
    def __init__(self, w, x, s):
        self.word = w
        self.posx = x
        self.posy = -100
        self.speed = s


class Session(object):
    def __init__(self):
        pass

class LoginoutSession(Session):
     def __init__(self):
        pass

class GameSession(Session):
    def __init__(self):
        self.word = wordManager.WordManager()


def main():
    ConnectionManager().start()

if __name__ == "__main__":
    main()
