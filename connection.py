import socket              # Import socket module

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        # Create a socket object
port = 8888                # Reserve a port for your service.

s.connect(("139.82.4.20", port))

for i in range(30):
  print(i)
  s.sendall(b'w')
  print(s.recv(1024))

s.close                    # Close the socket when done
