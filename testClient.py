import socket 
import struct

CLIENT = socket.gethostbyname(socket.gethostname())
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# if get a random port number
clientSocket.bind((CLIENT, 0))

msg ="""GET / HTTP/1.1
Host: reqbin.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36
Upgrade-Insecure-Requests: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate
"""

if __name__ == "__main__":
 clientSocket.connect((socket.gethostbyname(socket.gethostname()),5050))
 msg = bytes(msg,'utf-8')
 clientSocket.send(msg)
  
   

   