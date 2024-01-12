import socket
import threading

# Server configuration
SERVER_IP = '192.168.1.2'  # Replace with the actual IP address of the server
SERVER_PORT = 5555

# Create a socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER_IP, SERVER_PORT))

def receive_messages():
    while True:
        try:
            # Receive and display messages from the server
            data = client.recv(1024).decode('utf-8')
            print(data)
        except:
            # Handle errors, e.g., if the server closes unexpectedly
            print("Connection closed.")
            break

# Start a thread to receive messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Main loop to send messages
while True:
    message = input()
    client.send(bytes(message, 'utf-8'))
