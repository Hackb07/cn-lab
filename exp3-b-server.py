import socket

server = socket.socket()
server.bind(("localhost", 5000))
server.listen(1)

conn, addr = server.accept()
print("Connected:", addr)

with open("send.txt", "rb") as f:
    conn.sendall(f.read())

conn.close()
