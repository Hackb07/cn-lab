import socket

server = socket.socket()
server.bind(("localhost", 1234))
server.listen(1)

conn, addr = server.accept()
print("Connected:", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.send(data)   # Echo back

conn.close()
