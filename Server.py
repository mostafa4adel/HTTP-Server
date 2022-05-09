import re
import socket
import threading
import struct
from urllib import response
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
        message = message.decode('utf-8')
        message = splitResponse(message)
        if message[0][0] == "GET":
            requestedFileName = message[0][1]
            if requestedFileName == "/":
                requestedFileName = "index.html"
            
            try:
                with open(requestedFileName.replace('/','',1)) as f:
                    lines = f.readlines()
                response = f"HTTP/1.1 200 OK\r\n\r\n"
                for l in lines:
                    response = response + l
                client.send(bytes(response,'utf-8'))
                # print(response)
            except:
                response = f"HTTP/1.1 404 NOT FOUND\r\n"
                # print(response)
                client.send(bytes(response,'utf-8'))
            
        elif message[0][0] == "POST":
            fileName = message[0][1].replace('/','_')
            fileName = f"ServerFolder/{fileName}"
            f= open(fileName,"w+")
            f.write(message[-1])
            f.close()
            response = f"HTTP/1.1 200 OK\r\n\r\n"
            client.send(bytes(response,'utf-8'))
            
        print(f"Connection with {client} Closed!!!")
        client.close()

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
