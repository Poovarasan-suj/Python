import shutil
import os

src = "/home/sujith/Python/Day-19/shutil-copy.py"
dest = "/home/sujith/Python/Day-20/archive/"

if os.path.exists(src):
    print("File exists, proceeding copying to archive.")
    shutil.copy2(src, dest)
else:
    print("File does not exist, cannot copy.")