import socket
import struct

UDP_IP = "FF02::A:C:7:9"
UDP_PORT = 5005
# Message (boiler message)
MESSAGE = "This is a test"

sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
sock.bind(('', UDP_PORT))

group_bin = socket.inet_pton(socket.AF_INET6, UDP_IP)
group = group_bin + struct.pack('@I', 0)

sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_JOIN_GROUP, group)

while True:
    data, addr = sock.recvfrom(1024)
    print "recieved message:", data
