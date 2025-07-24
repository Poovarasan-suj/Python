import shutil
import os

src = "/home/sujith/Python/Day-19/log/report.log"
dest = "/home/sujith/Python/Day-20/archive/"

if os.path.exists(src):
    print("File exists, proceeding to move to archive.")
    shutil.move(src, dest)
else:
    print("File does not exist, cannot copy.")
    