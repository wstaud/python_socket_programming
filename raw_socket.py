from raw_socket_helper import RawSocket

# Constants
mymac = "\x00\x0c\x29\x07\xaf\x35"
myip = "\xC0\xA8\x00\x76"  #192.168.0.118"

# Layer 3 Header
#l3Field1 = ...
#l3Field2 = myip
#l3hdr = l3Field2

# Layer 2 Header
dst = mymac # Destination MAC
src = mymac # Source MAC
typ = '\x00\x00' # Ether Type, 0x0800 = IPv4
etherhdr = dst + src + typ

# Make the complete frame and send it
frame = etherhdr #+ l3hdr
interfaceName = "ens33" # from ifconfig
raw_socket = RawSocket(interfaceName)

# Makes it easy to find in wireshark
for i in range(10):
     raw_socket.send(frame) # Layer 2 has no checksums
      #raw_socket.send_chksum(frame) # Most higher layer proto
