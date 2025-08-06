import smtplib

sender_email = 'epoovarasansujith25@gmail.com'
receiver_email = 'epoovarasansujithe@gmail.com'
password = 'ohvr hnjk upjx jfhy' # Replace with your actual password

message = "Subject: Test Email\n\n This is a test email sent from Python!"

#Start SMTP Session

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
# Login to the email account
server.login(sender_email, password)
# Send the email
server.sendmail(sender_email, receiver_email, message)
# Close the SMTP session
server.quit()

print("Email sent successfully!")