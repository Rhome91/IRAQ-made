import socket
import sys
import time
from os import system
system("cls")
args = sys.argv
print("By Rhome91 (github)")
print(f"Start Scaning ON {args[1]}")
time.sleep(3)
open_ports = []
for port in range(int(args[2]), int(args[3])):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.001)
        sock.connect((args[1], port))
        open_ports.append(port)
        print(f"{port} [OPIN] {socket.getservbyport(port)}")
    except:
        print (f"{port} [CLOSE]")

print("---------------------------------------------------------")
for x in open_ports:
    print(f"{x} [OPIN]")
