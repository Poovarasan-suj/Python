
file_name = '/var/log/secure'

with open(file_name, 'r') as file:
    for line in file:
        if 'Failed password' in line:
            part = line.split()
            user = part[8]
            ip = part[10]
            print(f'User: {user}, IP: {ip}')
        elif 'Accepted password' in line:
            part = line.split()
            user = part[8]
            ip = part[10]
            print(f'User: {user}, IP: {ip}')    
      