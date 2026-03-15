
# Include nmap module
import nmap

# Create a PortScanner object
scanner = nmap.PortScanner()

#  Get the IP address of the vulnerable host
host = input("Enter the IP address of the vulnerable host to scan: ")

# Run a basic scan on the host
scanner.scan(host, '1-1024')


#Display the results of your scan
print("Host: ", host)
print("State: ", scanner[host].state())

# print("Open ports: ", scanner[host]['tcp'].keys())

# Check if TCP results exist
if 'tcp' in scanner[host]:
    open_ports = []

    for port in scanner[host]['tcp']:
        if scanner[host]['tcp'][port]['state'] == 'open':
            open_ports.append(port)

    if open_ports:
        print("Open ports:", open_ports)
    else:
        print("No open ports found.")
else:
    print("No open ports found.")