from itertools import count
import socket
import signal
import sys
import psutil
import asyncio
import time
from random import *

class colors:
    RED   = "\033[1;31m"
    YELLOW = "\033[1;33m"
    MAGENTA = "\033[35m"
    BLUE  = "\033[1;34m"
    CYAN  = "\033[1;36m"
    GREEN = "\033[1;32m"
    RESET = "\033[0;0m"
    BOLD    = "\033[;1m"
    REVERSE = "\033[1;7m"


def color_per(per):
    if per < 15:
        return colors.YELLOW + str(per)
    else:
        return colors.GREEN + str(per)
   

        

def signal_handler(sig, frame):
    print('\nDone!')
    sys.exit(0)

async def sleep(delay):
    await asyncio.sleep(delay)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit...')

##


tcp_port = 5005

ip_addr = str(input(colors.RED +("IP destino")+ colors.RESET + colors.RED + "(default ip_addr : 127.0.0.1): "))

if not ip_addr:
    ip_addr = "127.0.0.1"


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((ip_addr, tcp_port))
count=0

while True:
   
        try:
            time.sleep(2)
            message = colors.GREEN +"Percentage of memory in use:"
            message = message + colors.RESET + "\t\t" + color_per(psutil.virtual_memory()[2]) + "%\n"
            message = message + colors.YELLOW + "CPU utilization:"
            message = message + colors.RESET + "\t\t\t" + color_per(psutil.cpu_percent()) + "%\n"
            message = message.encode()
            if len(message)>0:
                sock.send(message)
                response = sock.recv(4096).decode()
        except (socket.timeout, socket.error):
            print('Server error. Done!')
            sys.exit(0)
