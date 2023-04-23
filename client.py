import socket

data_payload = 1024

try:
    port = int(input("Please input the port number of the server: "))
    if 1 <= port <= 65535:
        print("This is a VALID port number.")
    else:
        raise ValueError
except ValueError:
    print("This is NOT a VALID port number.")

host = input("Please input the host IP address: ")

while True:
    message = input("Enter a message to send to the server: ")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    print("Connecting to %s port %s" % server_address)
    sock.connect((host, port))
    sock.sendall(message.encode())

    if message == "x":
        break

    print("Sending %s" % message)
    data = sock.recv(data_payload)

    print("Received: %s" % data.decode('utf-8'))
    sock.close()

print("exit")
