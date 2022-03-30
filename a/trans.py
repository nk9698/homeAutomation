import sys
import socket
import os
import MySQLdb
db = MySQLdb.connect("localhost","root","123","fingeratten")
cur = db.cursor()

def internet_on():
        
        try:
            host=socket.gethostbyname("www.google.com")
            s=socket.create_connection((host,80),2)
            s.close()
            print ("ion")
            return 1
        except Exception:
            print("ioff")
        return 0
while 1:
        if internet_on()==1:
            db1 = MySQLdb.connect(host="208.91.198.197",user="srpeciot",passwd="Abc@12345",db="fingeratten")
            cur1 = db1.cursor()

            i=11
            while(i<16):
                cur.execute("SELECT * FROM asheet where id=%d",(i))
                abc=cur.fetchone();
                tlmaths=abc[2]
                almaths=abc[3]
                mathsper=abc[4]
                tlsci=abc[5]
                alsci=abc[6]
                sciper=abc[7]

                cur1.execute("UPDATE asheet set tlmaths=%d,almaths=%d,mathsper=%d where id=%d",(tlmaths,almaths,mathsper,i))
                cur1.execute("UPDATE asheet set tlsci=%d,alsci=%d,sciper=%d where id=%d",(tlsci,alsci,sciper,i))

        time.sleep(10)
                


            
        
                
                
