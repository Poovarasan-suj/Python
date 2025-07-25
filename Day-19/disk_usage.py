import shutil

usage = shutil.disk_usage("/")

print(f"Total Usage:{usage.total // (1024 ** 3) } GB" )
print(f"Used Usage: {usage.used // (1024 ** 3) } GB" )
print(f"Free Usage: {usage.free // (1024 ** 3) } GB" )