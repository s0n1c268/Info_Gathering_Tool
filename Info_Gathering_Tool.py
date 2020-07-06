#This script can be used for malicious activity, I am not liable for your actions!!!!
#This script was made for educational purposes!!!!

import socket
import threading
from queue import Queue

#=====================================

#Finds the Ip Address of the website

print("Made in collaboration with my friend, Cobra, please do check out his github: FURRO404")

target = str(input("Put in a website url please: "))

target_ip = socket.gethostbyname(target)

print("Website IP Address:", target_ip)

#=======================================

#Threaded Port Scanner
#Scans website for open ports from port 1-1000

print_lock = threading.Lock()

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target, port))
        with print_lock:
            print('port', port, 'is open!!')


        con.close

    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = Queue()

for x in range(500):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1,1001):
    q.put(worker)

q.join()
#=========================================

#Thanks again to my friend Cobra for collaborating with me on this project!!!!

