import zipfile

zipfile_name = '/home/sujith/Python/logs.zip'

#Decompress the zip file
with zipfile.ZipFile(zipfile_name, 'r') as zip_ref:
    zip_ref.extractall('/home/sujith/Python/logs')

print(f"Decompressed {zipfile_name} to /home/sujith/Python/logs")
# This script decompresses a zip file containing logs to a specified directory.