
import socket
import sys

HOST = '127.0.0.1' #localhost
PORT = 9999	# Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

#Bind socket to local host and port
try:
	s.bind((HOST, PORT))
except socket.error as msg:
	print('Bind failed. Error Code : ' + str(msg))
	sys.exit()
	
print('Socket bind complete')

#Start listening on socket
s.listen(10)
print('Socket now listening')

conn, addr = s.accept()
print('Connected with ' + addr[0] + ':' + str(addr[1]))

while True:
    #wait to receive data (blocking call)
	data = conn.recv(1024)

	if data == b'':
		print("Connection broken")
		break

	print("Received:")
	print(data)
	
s.close()