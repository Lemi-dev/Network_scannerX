# networkscan.py

import socket

def network_scan(ip_subnet_range, ports):
    results = []
    for ip in ip_subnet_range:
        for port in ports:
            try:
                # Create a socket object
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)  # Set a timeout for the socket connection

                # Attempt to connect to the IP and port
                result = sock.connect_ex((ip, port))
                if result == 0:
                    service = socket.getservbyport(port)
                    results.append({"host": ip, "port": port, "service": service})
                sock.close()
            except socket.error:
                pass
    return results