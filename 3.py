import socket
def echo_server():
# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET,
socket.SOCK_STREAM)
# Bind the socket to a specific address and port
server_socket.bind(('localhost', 65432))
# Listen for incoming connections
server_socket.listen(1)
print("Server listening on port 65432...")
# Accept a connection from a client
connection, client_address = server_socket.accept()
print(f"Connected by {client_address}")
while True:
# Receive the data from the client
data = connection.recv(1024)
if not data:
break # If no data, exit the loop
print(f"Received: {data.decode()}")
# Echo the data back to the client
connection.sendall(data)
connection.close()
if __name__ == '__main__':
echo_server()

#3b
import socket

def echo_client():
# Create a TCP/IP socket
client_socket = socket.socket(socket.AF_INET,
socket.SOCK_STREAM)
# Connect to the server
client_socket.connect(('localhost', 65432))
while True:
# Send data to the server
message = input("Enter a message: ")
client_socket.sendall(message.encode())
# Receive the echo response from the server
data = client_socket.recv(1024)
print(f"Echoed from server: {data.decode()}")
if message.lower() == 'exit':
break
client_socket.close()
if __name__ == '__main__':
echo_client()