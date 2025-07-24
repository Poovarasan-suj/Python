import os

try:
   if os.path.exists('logs'):
      print("Directory 'logs' already exists.")
   else:
      os.mkdir('logs')
      print("Directory 'logs' created successfully.")
except OSError as e:
   print(f"Error creating directory: {e}")     

file = '/home/sujith/Python/Day-18/data.txt'

if os.path.exists(file):
       print(f"File '{file}' exists.")
else:
       print(f"File {file} does not exist.")

       print(os.listdir())