# c2_server.py
import socket

HOST = "127.0.0.1"  # server ip
PORT = 2003

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"C2 server listening on {HOST}:{PORT}...")
        while True:  # Keep server running for multiple connections
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                data = conn.recv(1024)
                if data:
                    print(f"Received: {data.decode()}")

if __name__ == "__main__":
    start_server()