import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 8888))
sock.sendto(b'Client Message', ('127.0.0.1', 8888))
sock.close()
