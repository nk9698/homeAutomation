import serial
import MySQLdb
import os
import time
import datetime
import glob
from time import strftime
db = MySQLdb.connect(host="localhost",user="root",passwd="123",db="fingeratten")
cur = db.cursor()
ser = serial.Serial('/dev/ttyUSB0',9600)
while 1:
    read_serial=ser.readline()
    s = ser.readline()
    b="A"
    s1=len(s)
    print ("###############")
    DATE1 = time.strftime("%Y-%m-%d")
    #DATE1='2017-10-22'
    if s1 == 6:
        s=s[:4]
        print s
        if(s<=10 and s>=1):
            facsub=s
            cur.execute("SELECT subtl FROM facsub where id=%d",(s))
            row=cur.fetchone()
            d=row[0]
            d=d+1
            
            read_serial=ser.readline()
            s = ser.readline()
            s=s[:4]
            
            
            while(s>10):
                cur.execute("UPDATE facsub set subtl=%d where id=%d",(d,s))
                read_serial=ser.readline()
                s = ser.readline()
                s1=len(s)
                s=s[:4]
                
                if (s1==6 and s>10):
                    
                    if facsub==1:
                        cur.execute("SELECT almaths FROM student where id=%d",(s))
                        ab=cur.fetchone()
                        tal=ab[0]
                        tal=tal+1
                        cur.execute("UPDATE student set almaths=%d where id=%d",(tal,s))
                        cur.execute("INSERT INTO registor (id,date,maths) VALUES (%d,%s,1)",(s,DATE1))
                    if facsub==2:
                        cur.execute("SELECT alsci FROM student where id=%d",(s))
                        ab=cur.fetchone()
                        tal=ab[0]
                        tal=tal+1
                        cur.execute("UPDATE student set alsci=%d where id=%s",(s))
                        cur.execute("INSERT INTO registor (id,date,sci) VALUES (%d,%s,1)",(s,DATE1))

                        
                    
                
