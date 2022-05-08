
import string

# Rquest looks like this
# first line usually looks like this
# POST / HTTP/1.1 
# GET /background.png HTTP/1.0
# the first line contains method then url then the http version 
# 


def parseHTML(HTMLrequest:string):
 parsedRequest = HTMLrequest.split('/n')
 parsedRequest[0] = HTMLrequest.split(' ')
 return parsedRequest 




if __name__ == "__main__":
 pass