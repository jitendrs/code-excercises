#!/usr/binn/env python3


import socket
import subprocess
import sys
from datetime import  datetime


#clear the screen
subprocess.call("clear", shell=True)

# get input host
remoteServer = input("Enter a remote host to scan: ")
remoteServerIP = socket.gethostbyname(remoteServer)


print("-" * 60)
print("Please wait, scanning remote host:", remoteServerIP)
print("-" * 60)

t1 = datetime.now()


try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port)s
        if result == 0 :
            print("Port {}: Open".format(port))
        sock.close()
        
except KeyboardInterrupt:
    print("you pressed Cntrl+C")
    sock.exit()
    
except socket.gaierror:
    print("Hostname could not be resolved, Existing..")
    sys.exit()

except socket.error:
    print("Couldnn't connnect to server")
    sys.exit()

t2 = datetime.now()

total = t2 - t1
    
print("Scanning Completed: ", total)