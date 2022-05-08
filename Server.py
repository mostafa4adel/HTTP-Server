import socket
import threading
import struct
from HTMLParse import *


# ==================create server socket========================
HOST = socket.gethostbyname(socket.gethostname())
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# if port cause error change it
server.bind((HOST, 5050))
server.listen(5)
# ===============================================================


def handle(client):

    try:
        # waiting for client to send a message
        message = client.recv(1024)

        if message == "!DISCONNECT":
            # disconnect
            pass
        else:
            print(type(message))
            pass

    except:
        # Connection Lost Handle
        print(f"Connection Lost with {client}")


def receive():

    while True:

        # Accept Connections
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


if __name__ == "__main__":
    print(f"[LISTENING] Server is listening on {server}")
    receive()
