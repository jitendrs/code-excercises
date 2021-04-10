


"""
Calculate uptime for provided instance
"""
import time

def test_function():
    for i in range(1,5):
        time.sleep(i)



def get_uptime():
    start_time = time.perf_counter()
    print("Start time: ",start_time)
    test_function()
    end_time = time.perf_counter()
    print("Time difference is: ",end_time - start_time)



print(get_uptime())
"""
print("Seconds elapsed since the epoch are:", end=" ")
print(time.time())
print("Time calculated acc. to given seconds is:",time.gmtime())

t1 = time.time()
print("Time calculated using asctime is :", end=" ")
print(time.asctime())
print("Time calculated using ctime is: ", end=" ")
print(time.ctime())

print("Time calculated using strftime is:", time.strftime("%a, %d %b %Y %H:%M:%S",time.gmtime()))
"""