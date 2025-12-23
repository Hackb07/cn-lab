import socket

dns_server = ("8.8.8.8", 53)   # Google DNS
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

domain = input("Enter domain: ")

# Simple DNS query (A record)
query = b'\xaa\xaa\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00'
for part in domain.split('.'):
    query += bytes([len(part)]) + part.encode()
query += b'\x00\x00\x01\x00\x01'

sock.sendto(query, dns_server)
data, _ = sock.recvfrom(512)

print("DNS Response received (bytes):", data)
sock.close()
