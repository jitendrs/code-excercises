
import time


print("strptime calculation: ", time.strptime("Tue 12 Jan 2020 01:23:20","%a %d %b %Y %H:%M:%S"))
start_time = time.strptime("Tue 12 Jan 2020 01:23:20","%a %d %b %Y %H:%M:%S")
print("strptime calculation: ", time.strptime("Tue 12 Jan 2020 02:23:20","%a %d %b %Y %H:%M:%S"))
end_time = time.strptime("Tue 12 Jan 2020 02:23:20","%a %d %b %Y %H:%M:%S")
hr_sec = (end_time.tm_hour - start_time.tm_hour) * 3600
min_sec = (end_time.tm_min - start_time.tm_min) * 60
sec = (end_time.tm_sec - start_time.tm_sec)
print("Time difference is: ", (hr_sec + min-e) )