import subprocess
import time
import os

#set the Password
password = "test1234"
username = "demo3"

if subprocess.run(["id", username], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
    print(f"User {username} does not exist.")
    print("Creating user and setting password...")
    time.sleep(2)  # Wait for 2 seconds before proceeding
    # Create user and set password
    subprocess.run(["sudo", "useradd", username], check=True) 
    # Set the password for the user
    subprocess.run(["sudo", "chpasswd" ], input=f"{username}:{password}", text=True,  check=True)
    # add user to devops group
    subprocess.run(["sudo", "usermod", "-aG", "devops", username], check=True)
    print(f"User {username} created with password {password}")
else:
    print(f"User {username} already exists.")