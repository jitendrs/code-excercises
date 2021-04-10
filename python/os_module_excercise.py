import os

"""
basepath="."
for d in os.listdir():
   if os.path.isfile(os.path.join(basepath, d)):
       print(d)
"""

from  datetime import datetime as dt

def convert_timestamp(timestamp):
    d = dt.utcfromtimestamp(timestamp)
    formated_date = d.strftime("%d %b %Y %H:%M:%S")
    return formated_date


# with scandir
basepath="."
with os.scandir(basepath) as file_list:
    for f in file_list:
        if f.is_file():
            info = f.stat()
            print("{} Last modified: {}".format(f.name, convert_timestamp(info.st_mtime)))
            #print(info.st_mtime)
            #sprint(dir(f.stat()))
            #print(f.name)

