import socket
import time

host = '127.0.0.1'
port = 9999                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    print("Attempting to connect")
    try:
        s.connect((host, port))
        break
    except:
        time.sleep(0.25) # wait 5s and retry
        continue
    

while True:
    s.sendall(b"{from: \'ojf_server_py\', to: \'unity_server\', body: \'Tranquility Base here.\'}")
    print("Sent.")
    time.sleep(1)

data = s.recv(1024)
s.close()
print('Received', repr(data))