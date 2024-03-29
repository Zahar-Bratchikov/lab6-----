import socket
import sys

def start_client(host, port):
    # Создание сокета
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Подключение к серверу
        client_socket.connect((host, port))
        client_socket.settimeout(2)  # Устанавливаем таймаут в секундах

        print(f"Подключено к серверу {host}:{port}")

        while True:
            # Ввод данных с клавиатуры
            message = input("Введите данные для отправки (или 'exit' для выхода): ")
            if message.lower() == 'exit':
                break

            # Отправка данных серверу
            client_socket.sendall(message.encode('utf-8'))

            try:
                # Получение данных от сервера с использованием таймаута
                data = client_socket.recv(1024)
                if not data:
                    print("Сервер закрыл соединение")
                    break

                print(f"Получено от сервера: {data.decode('utf-8')}")

            except socket.timeout:
                print("Таймаут при получении данных от сервера")

    except KeyboardInterrupt:
        print("\nКлиент остановлен.")
    finally:
        # Закрытие сокета при завершении работы
        client_socket.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python tcp-client.py <ip-адрес> <порт>")
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    start_client(host, port)
