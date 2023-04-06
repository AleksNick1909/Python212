import socket

# папка ООП 8


def run():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 5000))
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)

        print(f"Клиент: {addr} => \n{request}\n")


if __name__ == '__main__':
    run()
