import shutil
import logging

usage = shutil.disk_usage('/')

logging.basicConfig(
    filename='my_disk.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

threshold = 80
used = (usage.used / usage.total) * 100

if used > threshold :
    #print(f" Used Usage has exceeded the threshold {threshold} %")
     logging.info(f'Used Usage has exceeded the threshold. current Usage{used:.2f} %')

else:
    #print("Root disk having enough space")
    #print(f"Current usage {used:.2f} %")
    logging.info(f'Root disk having enough space. current usage{used:.2f} %')   

