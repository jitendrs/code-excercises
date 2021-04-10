import calendar
from datetime import datetime as dt


today_date = dt.now()
print("Today's date:",today_date)

print("Year:", today_date.year)
print("Month:", today_date.month)
print("Day:", today_date.day)
print("Hour:", today_date.hour)
print("Minute:", today_date.minute)
print("Seconds:", today_date.second)



print(today_date.isocalendar())