#Task is Ping the host 


import subprocess


host = "192.168.56.101"

def ping_host(host):
    try:
        result = subprocess.run(["ping", "-c", "2", host], capture_output=True , text=True )

        if result.returncode == 0:
              print("[PING] Host is reachable")
        else:
              print("Host is unreachable")
    except:
        print("[PING] Error ")
ping_host(host)
