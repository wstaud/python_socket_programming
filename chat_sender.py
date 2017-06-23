import socket
import struct

PORT = 5005
UDP_IP = "FF02::A:C:7:9"
TTL = 5
MESSAGE = "THIS IS A TEST"

ttl_bin = struct.pack('@I', TTL)

# Socket Creation
sock = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_MULTICAST_HOPS, ttl_bin)

sock.sendto(MESSAGE, (UDP_IP, PORT))

