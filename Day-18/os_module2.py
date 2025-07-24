import os

print("My current working directories:", os.getcwd())

os.mkdir('test_dir') # Create new directory

print(os.listdir()) #List files and directories in the current directory

try:
   os.rmdir('test_dir') # Remove the directory
   print("Directory removed successfully")
except OSError:
    print("Directory not empty or does not exist")

print(os.path.exists('main.py')) # Check if a file exists