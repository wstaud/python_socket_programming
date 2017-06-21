from raw_socket_helper import RawSocket

interfaceName = "ens33"
raw_socket = RawSocket(interfaceName)

raw_socket.send(frame)
