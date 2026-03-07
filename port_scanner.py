import socket

def scan_ports(target, ports):
    print(f"Scanning {target}...\n")

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"Port {port}: OPEN")
        else:
            print(f"Port {port}: CLOSED")

        s.close()

target = input("Enter target IP or domain: ")

ports = [21, 22, 23, 25, 53, 80, 110, 443]

scan_ports(target, ports)
