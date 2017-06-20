import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
data = "This is a really realllly long string"

# convert dict to json string

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(data, (UDP_IP, UDP_PORT))
