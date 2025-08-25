#Task is Reading the AWS key from dotenv file and access the S3 bucket

import os

from dotenv import load_dotenv

#Load the dotenv file

load_dotenv()

#credentils

access_key = os.getenv('AWS_ACCESS_KEY_ID')

secret_key = os.getenv('AWS_SECRET_ACCESS_KEY')

region = os.getenv('AWS_DEFAULT_REGION')

#print

print(access_key)
print(secret_key)
print(region)










