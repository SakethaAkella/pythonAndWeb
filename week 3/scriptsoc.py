#Understanding the Request / Response Cycle
#Exploring the HyperText Transport Protocol
#You are to retrieve the following document using the HTTP protocol in a way that you can examine the HTTP Response headers.
#http://data.pr4e.org/intro-short.txt

import socket
import re

def parse_headers(response):
    headers = {}
    lines = response.split('\r\n')
    for line in lines:
        if ':' in line:
            key, value = line.split(':', 1)
            headers[key.strip()] = value.strip()
    return headers

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

header_data = b''
while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    header_data += data
    if b'\r\n\r\n' in header_data:
        break

headers = parse_headers(header_data.decode())

print('Last-Modified:', headers.get('Last-Modified'))
print('ETag:', headers.get('ETag'))
print('Content-Length:', headers.get('Content-Length'))
print('Cache-Control:', headers.get('Cache-Control'))
print('Content-Type:', headers.get('Content-Type'))

mysock.close()

#output
#Last-Modified: Sat, 13 May 2017 11:22:22 GMT
#ETag: "1d3-54f6609240717"
#Content-Length: 467
#Cache-Control: max-age=0, no-cache, no-store, must-revalidate
#Content-Type: text/plain