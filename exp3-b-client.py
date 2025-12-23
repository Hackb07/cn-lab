import socket

client = socket.socket()
client.connect(("localhost", 5000))

with open("received.txt", "wb") as f:
    data = client.recv(4096)
    f.write(data)

client.close()
