import socket
import threading
import signal
import sys



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

def signal_handler(sig, frame):
    print('\nDone!')
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)
print('Press Ctrl+C to exit...')

##

def handle_client_connection(client_socket,address): 

    print(colors.BLUE + 'Accepted connection from {}:{}'.format(address[0], address[1]))
    try:
        while True:
            request = client_socket.recv(1024)
            if not request:
                client_socket.close()
            else:
                msg=request.decode()
                print(msg)
                msg="\n".encode()
                client_socket.send(msg)
    except (socket.timeout, socket.error):
        print('Client {} error. Done!'.format(address))

ip_addr = "0.0.0.0"
tcp_port = 5005

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip_addr, tcp_port))
server.listen(5)  # max backlog of connections

print('Listening on {}:{}'.format(ip_addr, tcp_port))

while True:
    client_sock, address = server.accept()
    client_handler = threading.Thread(target=handle_client_connection,args=(client_sock,address),daemon=True)
    client_handler.start()