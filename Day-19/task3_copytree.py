import shutil
import os

src = "/home/sujith/Python/Day-19/projects/"
dest = "projects-backup"

if os.path.exists(src):
   print("Proceeding to copy the folder")
   
if not os.path.exists(dest):
    
        shutil.copytree(src , dest)
        print(f"{src} has been copied in {dest}")
else:
        print("Copied Failed")
    
