import socket

c = socket.socket()
c.connect(("localhost", 9000))
c.send(b"Hello using TCP")
c.close()
