import socket

IP = "127.0.1.1"
PORT = 1234
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((IP, PORT))


def send(msg):
    msg_length = len(msg)
    msg = msg.encode(FORMAT)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(msg)
    print(client.recv(2048).decode(FORMAT))


if __name__ == "__main__":
    send("HELLO, WORLD")
    input()
    send("HELLO, EVERYONE")
    input()
    send("HELLO, KETAN")
    input()
    send(DISCONNECT_MSG)