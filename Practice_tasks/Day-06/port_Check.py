#Task is to check the port whether opened or not for that using socket module

import socket

host ="192.168.56.101"
port = 22
def port_check(host , port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)

        result = sock.connect_ex((host , port))
        if result == 0:
              print(f"[Port] {port} is opened in {host}")
        else:
              print(f"[port] {port} is not open in {host}")
    except :
        print("[Port] Error")

port_check(host , port)
            


   
