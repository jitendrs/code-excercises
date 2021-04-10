


import re



with open("whoami.txt","r") as file:
    for line in file:
        x = re.split('\s+',line)
        #print(x[:-1])


import os


c = os.popen("who","r")
for line in c:
    print(line)