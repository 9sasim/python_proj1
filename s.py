import socket

def start_server():
    s = socket.socket()
    host = socket.gethostname()
    port = 8080
    s.bind((host, port))
    s.listen(1)
    print(host)
    print("Waiting for any incoming connections ... ")
    conn, addr = s.accept()
    print(addr, "Has connected to the server")
    return conn

def connect_to_server():
    s = socket.socket()
    host = input("Please enter the host name of the sender: ")
    port = 8080
    s.connect((host, port))
    print("Connected ... ")
    return s

def send_file(conn):
    filename = input("Please enter the filename of the file: ")
    file = open(filename, 'rb')
    file_data = file.read(1024)
    conn.send(file_data)
    print("Data has been transmitted successfully")
    file.close()

def receive_file(conn):
    filename = input("Please enter a filename for the incoming file: ")
    file = open(filename, 'rb')
    file_data = conn.recv(1024)
    file.write(file_data)
    file.close()
    print("File has been received successfully.")

def server_menu(conn):
    while True:
        print("\nServer Menu:")
        print("1. Send file")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            send_file(conn)
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

def client_menu(s):
    while True:
        print("\nClient Menu:")
        print("1. Receive file")
        print("2. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            receive_file(s)
        elif choice == '2':
            break
        else:
            print("Invalid choice. Please try again.")

conn = None
s = None

while True:
    print("\nMain Menu:")
    print("1. Start server")
    print("2. Connect to server")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        conn = start_server()
        server_menu(conn)
        conn.close()
    elif choice == '2':
        s = connect_to_server()
        client_menu(s)
        s.close()
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
