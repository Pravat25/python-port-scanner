import socket

def scan_ports(target, start_port, end_port):
    print(f"\nScanning target: {target}")
    print(f"Scanning ports {start_port} - {end_port}\n")

    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        result = s.connect_ex((target, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
            except:
                service = "Unknown"

            print(f"[OPEN] Port {port} ({service})")

        s.close()


target = input("Enter target IP or domain: ")
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

scan_ports(target, start_port, end_port)
