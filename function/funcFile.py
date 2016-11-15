import xlrd
import sqlite3

file = xlrd.open_workbook("function.xlsx")
con = sqlite3.connect('functions.sqlite3')
cur = con.cursor()

def main():
    makeC_table()
    makeJAVA_table()
    makePy_table()


def makePy_table():
    ws = file.sheet_by_index(0)

    cur.execute('DROP TABLE IF EXISTS PYTHON')
    cur.execute('CREATE TABLE PYTHON (FUNCTION TEXT)')

    nlow = ws.nrows
    
    i =0
    while i<nlow:
        cur.execute('INSERT INTO PYTHON (FUNCTION) VALUES (?)', [str(ws.row_values(i))])        
        i += 1

    con.commit()

    
def makeJAVA_table():
    ws = file.sheet_by_index(1)

    cur.execute('DROP TABLE IF EXISTS JAVA')
    cur.execute('CREATE TABLE JAVA (FUNCTION TEXT)')

    nlow = ws.nrows
    
    i =0
    while i<nlow:
        cur.execute('INSERT INTO JAVA (FUNCTION) VALUES (?)', [str(ws.row_values(i))])        
        i += 1

    con.commit()

    
def makeC_table():
    ws = file.sheet_by_index(2)

    cur.execute('DROP TABLE IF EXISTS C')
    cur.execute('CREATE TABLE C (FUNCTION TEXT)')

    nlow = ws.nrows
    
    i =0
    while i<nlow:
        cur.execute('INSERT INTO C (FUNCTION) VALUES (?)', [str(ws.row_values(i))])        
        i += 1

    con.commit()

__author__ = 'Administrator'

if __name__ == '__main__':
    main()
