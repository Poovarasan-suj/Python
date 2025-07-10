import sys

type = sys.argv[1]

if type == "t2.micro":
    print("Ok.It will charge 8 dollar per day")
elif type == "t2.medium":
    print("Ok it will charge 10 dollar per day")
elif type == "t2.xlarge":
    print("Ok It will charge 15 dollar per day")

else:
    print("please provide the valid type of instance")
