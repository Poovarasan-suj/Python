#Analysis Failed Login in secure log

log_file = '/var/log/secure'


with open (log_file , 'r') as file:
    for line in file:
        if "Failed password" in line:
           part = line.split()
           user = part[8]
           ip = part[10]
           month = part[0]
           date = part [1]


           print(f" {user} has tried login in the server from {ip} on {month} {date}")

     
