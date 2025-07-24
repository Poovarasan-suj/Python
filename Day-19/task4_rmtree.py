import shutil
import os

dest = "/home/sujith/Python/projects-backup"

if os.path.exists(dest):
    shutil.rmtree(dest)
    print(f"Removed the directory: {dest}")
else:
    print(f"The directory {dest} does not exist.")