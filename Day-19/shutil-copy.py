import shutil
import os

src = "/home/sujith/Python/Day-19"
dest = "/home/sujith/Python/Day-18/Day-19-copy"

if os.path.exists(dest):
        print(f"Directory {dest} already exists.")
else:
    shutil.copytree(src, dest)
    print(f"Directory copied from {src} to {dest}.")