import socket 

CLIENT = socket.gethostbyname(socket.gethostname())
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# if get a random port number
clientSocket.bind((CLIENT, 0))






if __name__ == "__main__":
 while True:
  command = input("Enter Command:")
  command = command.split('/n')[0]
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
   

   