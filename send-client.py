import socket
import sys

def start_send_client(server_host, server_port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        while True:
            message = input("Введите данные для отправки (или 'exit' для выхода): ")
            if message.lower() == 'exit':
                break

            # Отправка данных на заданный адрес и порт
            client_socket.sendto(message.encode('utf-8'), (server_host, server_port))

    except KeyboardInterrupt:
        print("\nКлиент отправки остановлен.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python send-client.py <ip-адрес сервера> <порт сервера>")
        sys.exit(1)

    server_host = sys.argv[1]
    server_port = int(sys.argv[2])
    start_send_client(server_host, server_port)
