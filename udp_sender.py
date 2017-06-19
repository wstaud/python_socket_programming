import socket
import json

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
example_dict = {'foo':1, 'bar':'qwerty', 'doge':'WOW'}

# convert dict to json string
MESSAGE = json.dumps(example_dict)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))