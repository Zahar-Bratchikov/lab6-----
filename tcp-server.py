import socket
import sys

def start_server(host, port):
    # Создание сокета
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Привязка сокета к указанному адресу и порту
        server_socket.bind((host, port))
        # Прослушивание входящих соединений
        server_socket.listen(1)
        print(f"Сервер запущен на {host}:{port}")

        while True:
            # Принятие входящего соединения
            connection, client_address = server_socket.accept()
            print(f"Подключение от {client_address}")

            # Получение данных от клиента
            data = connection.recv(1024)
            print(f"Получено: {data.decode('utf-8')}")

            # Отправка данных обратно клиенту
            connection.sendall(data)

    except KeyboardInterrupt:
        print("\nСервер остановлен.")
    finally:
        # Закрытие сокета при завершении работы
        server_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python tcp-server.py <ip-адрес> <порт>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    start_server(host, port)
