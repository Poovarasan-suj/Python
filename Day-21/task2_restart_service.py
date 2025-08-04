import subprocess

#Restarting the ssh service
print("Restarting the SSH service...")
subprocess.run(["sudo", "systemctl", "restart", "sshd"], check=True)
# Checking the status of the SSH service
print("Checking the status of the SSH service...")
subprocess.run(["sudo", "systemctl", "status", "sshd"], check=True)  
