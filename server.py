import socket


def server_program():
    host = socket.gethostname()
    port = 5000  

    server_socket = socket.socket()  
    
    server_socket.bind((host, port))  
    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
    ack = "ok"
    list = []
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("from connected user: " + str(data))
        list.append(str(data))
        conn.send(ack.encode())  

    print(list)
    conn.close()  


if __name__ == '__main__':
    server_program()
