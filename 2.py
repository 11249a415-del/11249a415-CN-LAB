import socket
# Create a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 8080))
server.listen(1)
print("HTTP Server running on http://localhost:8080 ...")
while True:
conn, addr = server.accept()
request = conn.recv(1024).decode()
print("--- Received HTTP Request ---")
print(request)
# Build a valid HTTP response string
http_response = (
"HTTP/1.1 200 OK\r\n"
"Content-Type: text/html; charset=utf-8\r\n"
"Connection: close\r\n"
"\r\n"
"<html><body><h1>welcome to Computer networks Lab!</h1></body></html>"
)
# Send the HTTP response and close
conn.sendall(http_response.encode())
conn.close()


#2b

import socket
# Create a TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 8080))
# Create a basic HTTP GET request
http_request = (
"GET / HTTP/1.1\r\n"
"Host: localhost\r\n"
"Connection: close\r\n"
"\r\n"
)
# Send the request to the HTTP server
client.sendall(http_request.encode())
# Gather all data sent back by the server
response = b""
while True:
chunk = client.recv(1024)
if not chunk:
break
response += chunk
print("--- Received HTTP Response ---")
print(response.decode())
client.close()

