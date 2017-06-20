import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    dataList = data.split()
    dataList = sorted(dataList, key = len, reverse = True)
    data = " ".join(dataList)

    print "recieved message:", data
    print type(data)
    print "Sending to next socket"

    sock.sendto(data, (UDP_IP, UDP_PORT + 1))

