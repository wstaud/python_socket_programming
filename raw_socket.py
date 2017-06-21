from raw_socket_helper import RawSocket
import struct
import socket

# Constants
mymac = "\x00\x0c\x29\x07\xaf\x35"
myip = "\xC0\xA8\x00\x76"  #192.168.0.118"
dest_ip = "\xC0\xA8\x00\x74"  #192.168.0.116"

# Layer 2 Header
dst = mymac # Destination MAC
src = mymac # Source MAC
# typ = '\x00\x00' # Ether Type, 0x0800 = IPv4
typ = 0x0806
# etherhdr = dst + src + typ
etherhdr = struct.pack("!6s6sH", dst, src, typ)


# ARP header
htype = 1
ptype = 0x0800
hlen = 6
plen = 4
operation = 1
src_ip = myip
dst_ip = dest_ip
arp_hdr = struct.pack("!HHBBH6s4s6s4s", htype, ptype, hlen, plen, operation, src , src_ip, dst, dst_ip)


# Make the complete frame and send it
frame = etherhdr + arp_hdr 
interfaceName = "ens33" # from ifconfig
raw_socket = RawSocket(interfaceName)

# Makes it easy to find in wireshark
for i in range(5):
     raw_socket.send(frame) # Layer 2 has no checksums
