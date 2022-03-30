
import socket
import MySQLdb
import os
import time

db = MySQLdb.connect(host="localhost",user="root",passwd="",db="123456")
cur = db.cursor()


cur.execute("SELECT string from string where id=1")
aut=cur.fetchone()
at=aut[0]
print at
while 1:

    cur.execute("SELECT string from string where id=1")
    aut1=cur.fetchone()
    at1=aut[0]
    if(at!=at1):
        print at1
        at=at1
        
    
    
