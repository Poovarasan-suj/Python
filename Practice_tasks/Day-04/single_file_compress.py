import zipfile

zip_name = 'test.zip'

with zipfile.ZipFile(zip_name, 'w') as zfile:
    zfile.write('test')
  
