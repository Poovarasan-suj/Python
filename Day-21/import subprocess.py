import subprocess

print("Typing Wrong Command: ")
try:
    subprocess.run(["wrong_command"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Command failed with error: {e}")