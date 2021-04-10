"""
Date parser 
"""

from datetime import datetime

now = datetime.now()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
min = str(now.minute)
sec = str(now.second)

print(dd + "/" + mm + "/" + yyyy + " " + hour + ":" + min + ":" + sec)