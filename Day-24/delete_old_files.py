import os

import time

folder_path = '/home/sujith/Python/logs' #Log location
days_to_keep = 7  # Number of days to keep files
now  = time.time() # Current time in seconds since epoch

# Iterate through all files in the directory
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path , filename)

    if os.path.isfile(file_path):
        file_mtime = os.path.getmtime(file_path)

        if (now - file_mtime) > ( days_to_keep * 86400):
           os.remove(file_path)
           print("Deleted 7 days older files")
        else:
           print("Files less than 7 days older")
   
