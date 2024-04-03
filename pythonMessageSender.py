import socket
import threading

def start_server(host, port):
    #Create socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        #Bind socket to port and host
        server_socket.bind((host, port))

        #Start listening for connections
        server_socket.listen(1)
        print(f"Server listening on {host}:{port}")

        while True:
            # Accept incoming connection
            client_socket, client_address = server_socket.accept()
            print(f"Connection established from {client_address}")

            # Receive data from the client
            data = client_socket.recv(1024).decode()
            print(f"Received message: {data}")

            # Close the connection
            client_socket.close()

    except Exception as e:
        print(f"Error occurred while running server: {e}")

    finally:
        # Close the server socket
        server_socket.close()

def send_message(message, target_ip, target_port):
    # Create socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the target IP and port
        sock.connect((target_ip, target_port))

        # Send message
        sock.sendall(message.encode())
        print("Message sent successfully.")

    except Exception as e:
        print(f"Error occurred while sending message: {e}")

    finally:
        # Close socket
        sock.close()

if __name__ == "__main__":
    target_ip = "<ip>" #adjust values here
    target_port = 9999

    # Message
    message = "This is a message from the sender!"

    # Start server in separate thread
    server_thread = threading.Thread(target=start_server, args=("0.0.0.0", 9999))
    server_thread.start()

    # Send message
    send_message(message, target_ip, target_port)
