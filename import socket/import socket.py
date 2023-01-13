import socket
import time

def port_scanner(hostname, port, timeout):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        start_time = time.time()
        result = sock.connect((hostname, port))
        end_time = time.time()
        print(f"Port {port} is open on {hostname}.")
        sock.shutdown(2)
        print("Service name: " + str(socket.getservbyport(port)) + " , Port name: " + str(socket.getprotobyname(socket.getservbyport(port))))
        print("Time to establish connection : " + str(end_time - start_time) + " sec")
        return True
    except:
        return False

hostname = input("Please enter the hostname or IP address: ")
start_port = int(input("Please enter the starting port number: "))
end_port = int(input("Please enter the ending port number: "))
timeout = int(input("Please enter the timeout duration (in seconds): "))

open_ports = []

for port in range(start_port, end_port+1):
    if port_scanner(hostname, port, timeout):
        open_ports.append(port)

if len(open_ports) > 0:
    print(f"Open ports on {hostname} : {open_ports}")
else:
    print(f"No open ports were found on {hostname}.")