import zipfile

files_compress = ['f1.txt' , 'f2.txt' , 'f3.txt']


with zipfile.ZipFile("mutiple.zip" , 'w') as zipf:
    for file in files_compress:
        zipf.write(file)
    print("All the files has been compressed")
