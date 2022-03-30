import MySQLdb
import os
import time
import datetime
import glob
from time import strftime
db1 = MySQLdb.connect(host="localhost",user="root",passwd="123",db="fingeratten")
cur1 = db1.cursor()

    
while 1:

    cur1.execute("SELECT subtl FROM facsub where id=1")
    row1=cur1.fetchone()
    subtlmaths=row1[0]
    cur1.execute("SELECT subtl FROM facsub where id=2")
    row2=cur1.fetchone()
    subtlsci=row2[0]


    i=11
    while(i<16):
        
        cur1.execute("SELECT * FROM student where id=%d",(i))
        abc=cur1.fetchone()
        almaths=abc[2]
        alsci=abc[3]

        mathsper=(almaths*100)/subtlmaths
        sciper=(alsci*100)/subtlsci
        cur1.execute("UPDATE asheet set tlmaths=%d,almaths=%d,mathsper=%d where id=%d ",(subtlmaths,almaths,mathsper,i))
        cur1.execute("UPDATE asheet set tlsci=%d,alsci=%d,sciper=%d where id=%d ",(subtlsci,alsci,sciper,i))

        i=i+1
    time.sleep(30)
        
        
          
