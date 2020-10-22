import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
sock.sendto(b'Unix test message', 'unix.sock')
