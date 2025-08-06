import shutil 
import smtplib
import logging

logging.basicConfig(filename='disk_usage.log', level=logging.WARNING, format='%(asctime)s - %(levelname)s - %(message)s')  

sender_email = 'epoovarasansujith25@gmail.com'
receiver_email = 'epoovarasansujithe@gmail.com'
password = 'ohvr hnjk upjx jfhy' # Replace with your actual password

message = """Subject : Warning - Disk Usage Alert

Hello,

This is an automated alert from your disk monitoring system.
Please be advised that the disk usage has exceeded the defined threshold.
This is a warning to take necessary actions.

Best regards,
Disk Monitoring System

Note: This is an automated message. Do not reply to this email.
 Disk usage is above Threshold. Please check your system."""

threshold = 20
usage = shutil.disk_usage('/')

current_usage = usage.used / usage.total * 100
if current_usage > threshold:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
    server.quit()
    logging.warning(f"Disk usage is above {threshold}%: {current_usage:.2f}%")
else:
    print("Disk usage is within the threshold.")



