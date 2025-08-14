import shutil
import psutil

#This function for obtain the disk usage and free 

def get_disk_usage():
    usage = shutil.disk_usage("/")
    total = usage.total / (1024 ** 3)
    free = usage.free / (1024 ** 3)
    used = usage.used / (1024 ** 3)
    return (f"Disk is currently used {used:.2f} GB out of {total:.2f} GB")
get_disk_usage()

def get_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    return(f"Cpu Usage: {cpu_percent} %")
get_cpu_usage()

if __name__ == "__main__":
    get_disk_usage()
    get_cpu_usage()

