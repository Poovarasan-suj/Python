#Task to find the ip address of domain 

import socket

domain = 'googlel.com'

def dns_lookup(domain):
 try:
    ip = socket.gethostbyname(domain)
    print(f"DNS Lookup : Domain >> {ip}")
 except socket.gaierror:
    print("[DNS] domain not found")
dns_lookup(domain)

