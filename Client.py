import socket


def client_program():
    host = socket.gethostname()  
    port = 5000 

    client_socket = socket.socket()  
    client_socket.connect((host, port))  
    message = [1,2,3,4,5,6,7,8,9,10]
    
    i =0
    while i<10:
        client_socket.send(str(message[i]).encode())
        data = client_socket.recv(1024).decode()
        if str(data) == "ok":
            i = i+1
          

    client_socket.close()  


if __name__ == '__main__':
    client_program()
