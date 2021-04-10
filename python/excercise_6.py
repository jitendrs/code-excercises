

import psutil

ps_p = psutil.cpu_percent()
ps_m = psutil.virtual_memory()

print("CPU:",ps_p)
print("MEMORY:",ps_m)