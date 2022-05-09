from cgi import print_environ
import socket 


if __name__ == "__main__":
  while True:
    commandFile = input("Enter File Name : ")
    commands = []
    with open(commandFile) as f:
      lines = f.readlines()
      for l in lines:
        if '\n' in l:
          l = l[:-1]
        commands.append(l)
    print(commands)
      
    for command in commands:
      CLIENT = socket.gethostbyname(socket.gethostname())
      clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      
      command = command.split(' ')
    
      if len(command) < 3:
        print("Error in Command")
        continue
    
      if len(command) >= 3:
        if command[0].lower() != 'get' and command[0].lower() != 'post':
          print('Unhandled Command')
          continue
      
      if command[0].lower() == 'get':
        FILE_NAME = command[1]
        HOST = command[2]
        HOSTPort = 80 if len(command)<4 else command[3]
        request = f"GET {FILE_NAME} HTTP/1.1\r\nHost: {HOST}:{HOSTPort}\r\n\r\n"
        print(f"Connect to {HOST} port = {HOSTPort}")
        clientSocket.connect((HOST,HOSTPort))
        #  response = clientSocket.recv(1024)
        #  print(response.decode('utf-8'))
        clientSocket.send(bytes(request,'utf-8'))  
        response = clientSocket.recv(1024)
        print(response.decode('utf-8'))  
        
        clientSocket.close()
