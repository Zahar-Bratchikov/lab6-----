import socket
import sys

def start_receive_client(local_port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('0.0.0.0', local_port))  # Привязка к любому доступному интерфейсу

    try:
        print(f"Сервер получения запущен на порту {local_port}")

        while True:
            # Получение данных
            data, addr = server_socket.recvfrom(1024)
            print(f"Получено от {addr}: {data.decode('utf-8')}")

    except KeyboardInterrupt:
        print("\nСервер получения остановлен.")
    finally:
        server_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python receive-client.py <порт>")
        sys.exit(1)

    local_port = int(sys.argv[1])
    start_receive_client(local_port)
