import os

import shutil

src = "/home/sujith/Python/Day-19/input/"
dest ="/home/sujith/Python/Day-19/output/"

if os.path.exists(dest):
  shutil.rmtree(dest)
  print("Output directory already exists. removindg file under ouptput directory")
else:
  print("Output directory does not exist. Creating output directory")
  os.makedirs(dest)

for file in os.listdir(src):
      src_path = os.path.join(src, file)

if os.path.isfile(src_path):
        # Copy the file to the destination directory
        print(f"Copying {file} to {dest}")
        shutil.copy(os.path.join(src, file), dest)
        print(f"Copied {file} to {dest}")
else:
        print(f"Skipping {file}, as it is not a file.")
    
print( "All files copied successfully.")     