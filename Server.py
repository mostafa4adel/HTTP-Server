import socket
import threading



#==================create server socket========================
HOST = socket.gethostbyname(socket.gethostname())
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# if port cause error change it
server.bind((HOST, 5050))
server.listen(5)
#===============================================================


def handle(client):
    while True:
        try:
            #waiting for client to send a message
            message = client.recv(1024)
            if message == "!DISCONNECT":
             #disconnect
             pass
            else:
             #handle client
             pass
        except:
            # Connection Lost Handle 
            print(f"Connection Lost with {client}")
            break


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
