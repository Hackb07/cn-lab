import socket

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
c.sendto(b"Hello using UDP", ("localhost", 9001))
