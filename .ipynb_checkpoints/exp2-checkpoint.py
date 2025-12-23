import socket

# Create TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to web server (HTTP uses port 80)
client.connect(("pmctech.org", 80))

# HTTP GET request
request = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"
client.send(request.encode())

# Receive response
response = client.recv(4096)

# Print response
print(response.decode())

# Close connection
client.close()
