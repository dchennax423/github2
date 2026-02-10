import psutil
import sys

CPU_LIMIT = 80
MEM_LIMIT = 90
DISK_LIMIT = 90

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

print("---- Server Health Report ----")
print(f"CPU Usage    : {cpu}%")
print(f"Memory Usage : {memory}%")
print(f"Disk Usage   : {disk}%")

if cpu > CPU_LIMIT:
    print("❌ CPU usage high")
    sys.exit(1)

if memory > MEM_LIMIT:
    print("❌ Memory usage high")
    sys.exit(1)

if disk > DISK_LIMIT:
    print("❌ Disk usage high")
    sys.exit(1)

print("✅ Server is healthy")
sys.exit(0)
