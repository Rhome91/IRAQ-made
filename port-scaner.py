import socket
import sys
import time
from os import system
system("clear")
args = sys.argv
print("By Rhome91 (github)")
print(f"Start Scaning ON {args[1]}")
time.sleep(2)
open_ports = []
for port in range(int(args[2]), int(args[3])):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.000001)
        sock.connect((args[1], port))
        open_ports.append(port)
        print(f"{port} \33[1;32m[OPIN] {socket.getservbyport(port)}")
    except:
        print (f"{port} \33[1;31m[CLOSE]")

print("\33[1;33m---------------------------------------------------------")
for x in open_ports:
    print(f"{x} \33[1;32m[OPIN]")
