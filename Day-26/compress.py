import zipfile
import os

#file location
file_location = "/home/sujith/Python/logs"
# Create a zip file
zipfile_name = '/home/sujith/Python/logs.zip'

with zipfile.ZipFile(zipfile_name, 'w') as myzip:
    for root, dirs, files in os.walk(file_location):
        for file in files:
            file_path = os.path.join(root, file)
            myzip.write(file_path, os.path.relpath(file_path, file_location))
            print(f"Added {file_path} to the zip file.")
print("Zip file created successfully.")