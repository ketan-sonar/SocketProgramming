import socket
import threading

IP = socket.gethostbyname(socket.gethostname())
PORT = 1234
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] CONNECTED TO { addr }...")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False
            print(f"[{ addr }] { msg }")
            conn.send("MESSAGE RECEIVED".encode(FORMAT))
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] STARTED LISTENING AT { IP }:{ PORT }...")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] { threading.activeCount() - 1 }")


if __name__ == "__main__":
    print("[STARTING] THE SERVER IS STARTING...")
    start()