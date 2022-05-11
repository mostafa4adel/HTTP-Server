import socket
import threading
import time



maxNumberOfClients = 10

# ==================create server socket========================
HOST = socket.gethostname()
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# if port cause error change it
server.bind((HOST, 5050))
server.listen(maxNumberOfClients)
# ===============================================================

timeoutInSec = 15
clients = []
clientsDictionary = {}




def handle(client):
    exitLoop = False
    while True:
        if exitLoop:
            break
        try:
            # waiting for client to send a message
            message = client.recv(1024)
            message = message.decode('utf-8')
            
            if len(message) == 0:
                print(f"Client:{client} Lost Connection")
                client.close()
                break
            
            clientsDictionary[client] = time.time()
            message = splitResponse(message)
            if message[0][0] == "GET":
                requestedFileName = message[0][1]
                if requestedFileName == "/":
                    requestedFileName = "index.html"
                
                try:
                    requestedFileName = requestedFileName.replace('/','',1)
                    with open(requestedFileName.replace('/','_')) as f:
                        lines = f.readlines()
                    response = f"HTTP/1.1 200 OK\r\n\r\n"
                    for l in lines:
                        response = response + l
                    client.send(bytes(response,'utf-8'))
                    # print(response)
                except:
                    
                    response = f"HTTP/1.1 404 NOT FOUND\r\n\r\n"
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
            
            
        except:
            # Connection Lost Handle
            print(f"Connection Closed with {client}")
            
            break
            


def receiveClients():

    while True:

        # Accept Connections
        client, address = server.accept()
        print("Connected with {}".format(str(address)))
        
        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        clients.append((client,time.time()))
        clientsDictionary[client] = time.time()
        thread.start()
        
        

def http1_1Support():
    #just keep looping to monitor the clients
    while True: 
    
        for client in clients:
            if abs(clientsDictionary[client[0]]- time.time()) > timeoutInSec:
                client[0].close()
                clients.remove(client)
        

if __name__ == "__main__":
    print(f"[LISTENING] Server is listening on {server}")
    thread1 = threading.Thread(target=receiveClients, args=())
    thread2 = threading.Thread(target=http1_1Support,args = ())
    thread1.start()
    thread2.start()


    while True:
        timeoutInSec = timeoutInSec - (maxNumberOfClients * timeoutInSec)/(len(clients)+1) + 2
        # 2 is the min value



#[(<socket.socket [closed] fd=-1, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0>, 1652281275.6386073, <Thread(Thread-3, stopped 19984)>)]