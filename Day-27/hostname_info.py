
import socket
import datetime
import getpass
#Get the hostname of the server , date and user info.

hostname = socket.gethostname()
today = datetime.datetime.now()
user = getpass.getuser()
ipaddress = socket.gethostbyname(hostname)
print(hostname)
print(f"Today : {today.strftime('%Y-%m-%d')}")
print(f"Time : {today.strftime('%H:%M:%S')}")
print(f"Current logged user : {user}")
print(f"IP Address : {ipaddress}")


