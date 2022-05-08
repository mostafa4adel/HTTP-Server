
import string

# Rquest looks like this
# first line usually looks like this
# POST / HTTP/1.1 
# GET /background.png HTTP/1.0
# the first line contains method then url then the http version 
# 
msg ="""GET / HTTP/1.1
Host: reqbin.com
Connection: keep-alive
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36
Upgrade-Insecure-Requests: 1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Language: en-US,en;q=0.9
Accept-Encoding: gzip, deflate
"""


def parseHTML(HTMLrequest:string):
 parsedRequest = HTMLrequest.split('\n')
 parsedRequest[0] = parsedRequest[0].split(' ')
 
 
 return parsedRequest 




if __name__ == "__main__":
 msg = parseHTML(msg)
 print(msg[0][0])