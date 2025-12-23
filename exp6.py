# Simulated ARP Table
arp_table = {
    "192.168.1.1": "AA:BB:CC:DD:EE:01",
    "192.168.1.2": "AA:BB:CC:DD:EE:02",
    "192.168.1.3": "AA:BB:CC:DD:EE:03"
}

ip = input("Enter IP address: ")

if ip in arp_table:
    print("MAC Address:", arp_table[ip])
else:
    print("ARP Request Broadcasted")
    print("No entry found in ARP table")
