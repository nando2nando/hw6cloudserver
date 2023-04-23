import socket

data_payload = 2048
backlog = 5


def echo_server(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_address = (host, port)
    print("Starting up echo server on %s port %s" % server_address)
    sock.bind((host, port))
    sock.listen(backlog)

    while True:
        print("Waiting to receive message from client")
        client, address = sock.accept()
        data = client.recv(data_payload)
        print("Received Data: %s" % data.decode('utf-8'))  # decode data received from client

        if data and data.decode('utf-8') != "x":
            upper_data = data.upper()
            client.send(upper_data)
            print("Sent %s bytes back to %s" % (len(data), address))  # print length of data sent

        if data.decode('utf-8') == "x":
            print("exit")
            break

    client.close()
    sock.close()


if __name__ == '__main__':
    host = input("Please input your IP address: ")
    port = int(input("Please input the port number: "))
    echo_server(host, port)
