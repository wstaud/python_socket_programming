from raw_socket_helper import RawSocket_IPv6
import socket
import struct

# Constants
mymac = "\x00\x0c\x29\x07\xaf\x35"
myip = "\x0a\x0c\x07\x09\x00\x00\x00\x50" # a:c:7:9::50 
dest_ip = "\x0a\x0c\x07\x09\x00\x00\x00\x50"  

# Layer 2 Header
dst = mymac # Destination MAC
src = mymac # Source MAC
typ = 0x86DD
# typ = '0x86DD'
# etherhdr = dst + src + typ
etherhdr = struct.pack("!6s6sH", dst, src, typ)

# IPv6 Header
Ver_traffic_flow = '\x60\x00\x00\x00'
PayloadLength = '\x00\x23\x3A\x05' #payloadLength next header - hop length
ipv6hdr = Ver_traffic_flow + PayloadLength + myip + dest_ip

# ICMPv6 Header
Type = '\x87'
Code = '\x00'
check = '\x00\x00'
icmpv6hdr = Type + Code + check

# Make the complete frame and send it
frame = etherhdr + ipv6hdr + icmpv6hdr 
interfaceName = "ens33" # from ifconfig
raw_socket = RawSocket_IPv6(interfaceName)


# Makes it easy to find in wireshark
for i in range(5):
     raw_socket.send_chksum(frame) 
