#Automate the user creation process
import subprocess
import os

#Username
username = 'demo_user'
try:
    subprocess.run(["sudo" , "useradd", username], check=True)
    print(f"User {username} created successfully")
except subprocess.CalledProcessError:
        print(f"An error occurred while creating user {username}")

