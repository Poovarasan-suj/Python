import os

folders = input("Please provide the names of folders: ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
       print("Kindly provide the valid folder, it doesnt exist the folder - " + folder)
       continue
    print("Listing the files under" + folder)
    for file in files:
     print(file)