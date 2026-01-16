import socket
import sys

print("=========================================")
print("Basic Socket Command Server")
print("=========================================")

if len(sys.argv) != 3:
    print("Usage: python server.py <host> <port>")
    sys.exit(1)

HOST = sys.argv[1]
PORT = int(sys.argv[2])

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)

print("[*] Listening for incoming connection...")
conn, addr = server.accept()
print("[+] Connection from:", addr)

while True:
    command = input("shell> ")

    if command.lower() == "exit":
        print("Closing connection...")
        conn.send(b"exit")
        break

    conn.send(command.encode())
    output = conn.recv(4096).decode()
    print(output)

conn.close()
server.close()

print("\n=========================================")
print("Developed by sudo_0xksh")
print("=========================================")
