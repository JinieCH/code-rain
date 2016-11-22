import sqlite3, threading


class LockableCursor:
    def __init__ (self, cursor):
        self.cursor = cursor
        self.lock = threading.Lock()

    def execute (self, arg0, arg1 = None):
        self.lock.acquire()

        try:
            self.cursor.execute(arg1 if arg1 else arg0)

            if arg1:
                if arg0 == 'all':
                    result = self.cursor.fetchall ()
                elif arg0 == 'one':
                    result = self.cursor.fetchone ()
        except Exception as exception:
            raise exception

        finally:
            self.lock.release()
            if arg1:
                return result

class DBConnector(object):
    def __init__(self):
        # initialize database
        self.db_name = None
        self.db_connect = None
        self.cursor = None

    def transection(self, string):
        if self.isOpen():
            return self.cursor.execute('one', string)
        else:
            return False
    
    def createTable(self, table_name, attribute1, type1, attribute2, type2):
        self.transection('CREATE TABLE IF NOT EXISTS {} ({} {}, {} {})'.format(table_name, attribute1, type1, attribute2, type2))

    def insert(self, table_name, attribute1, attribute2, data):
        if self.transection('INSERT INTO {} ({}, {}) VALUES (\'{}\', \'{}\')'
                            .format(table_name, attribute1, attribute2, data[0], data[1])):
            return True
        else:
            return False

    def read(self, table_name, attribute1, attribute2, data):
        data = self.transection('SELECT * FROM {} WHERE {}=\'{}\' AND {}=\'{}\''
                                   .format(table_name, attribute1, data[0], attribute2, data[1]))
        if data:
            return data
        else:
            return False

    def delete(self, table_name,attribute1, attribute2, data):
        if self.transection('DELETE FROM {} WHERE {}=\'{}\' AND {}=\'{}\''
                            .format(table_name, attribute1, data[0], attribute2, data[1])):
            return True
        else:
            return False

    def update(self, table_name, attribute1, attribute2, data):
        if self.transection('UPDATE {} SET {} = \'{}\' WHERE {} = \'{}\''
                            .format(table_name, attribute1, data[0], attribute2, data[1])):
            return True
        else:
            return False

    def open(self, name):
        self.close()
        self.db_name = name
        self.db_connect = sqlite3.connect(self.db_name, check_same_thread = False, isolation_level = None)
        self.cursor = LockableCursor(self.db_connect.cursor())

    def isOpen(self):
       if self.db_connect:
           return True
       else:
           return False

    def close(self):
        if self.isOpen():
            self.db_connect.close()
