import os

from dotenv import load_dotenv
# This script loads AWS access and secret keys from an environment file (.env)

#Read the env file form this location

load_dotenv()

#Create the variable for keys

access_key = os.getenv("Aws_Access_Key")
secret_key = os.getenv("Aws_Secret_key")

#Mask the key 
def mask_key(key):
    return key[:4] + "*********"



#Print the keys

print("Aws_access_key:", mask_key(access_key))
print("Aws_secret_key:", mask_key(secret_key))

