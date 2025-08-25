import zipfile
import os
folders = '/var/log'

zip_name = "log_backup.zip"


with zipfile.ZipFile(zip_name , 'w') as zipf:
    for root, dirs,files in os.walk(folders):
        for file in files:
            file_path = os.path.join(root , file)
            zipf.write(file_path)
    print("Folder has been compressed successfully")
