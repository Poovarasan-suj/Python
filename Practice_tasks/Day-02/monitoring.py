#Disk Monitoring 

import shutil
import logging
import smtplib

#Smtp Details

sender_mail = 'epoovarasansujith25@gmail.com'
receiver_mail = 'epoovarasansujithe@gmail.com'
password = 'twjk jwja psco oovf'

message = """ Subject : Warning - Disk Usage report
 
Hello Team,

  Disk is currently over Utilised and kindly check!!

"""

logging.basicConfig(
        filename ='disk.log',
        level = logging.INFO,
        format='%(asctime)s - %(levelname)s -%(message)s'
        )
threshold = 20 
usage = shutil.disk_usage('/')

total = usage.total / ( 1024 ** 3) 
used = usage.used / ( 1024 ** 3 )
free = usage.free / ( 1024 ** 3 )

current = used / total * 100
if current > threshold :
     #Sending Mail
     server = smtplib.SMTP('smtp.gmail.com', 587)
     server.starttls()
     server.login(sender_mail , password)
     server.sendmail(sender_mail, receiver_mail , message)
     server.quit()
     print("Mail Sent Successfully")
     logging.info(f"Total disk is {total:.2f} GB, currently used is more than  threshold  {used:.2f} GB , Kindly check and increase the disk")
else:
    logging.info(f"The current usage is {current} % , It is less the threshold")


#Cpu Monitoring

import psutil

threshold_cpu = 50

cpu_percent = psutil.cpu_percent(interval=1)

if cpu_percent > threshold_cpu :

    logging.info(f"CPU is currently {cpu_percent} % , It is More than threshold , Kindly check !!")
else:
    logging.info("CPU is Normal")

