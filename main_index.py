from http.server import BaseHTTPRequestHandler, HTTPServer
import os


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Определяем базовый путь к статическим файлам
        base_path = os.path.join(os.getcwd(), 'dist')

        # Определяем путь к запрашиваемому файлу
        path = self.path
        if path == '/':
            path = '/contacts.html'

        # Формируем полный путь к файлу
        full_path = os.path.join(base_path, path[1:])

        try:
            # Проверяем существование файла
            if not os.path.exists(full_path):
                self.send_error(404, "File not found!")
                return

            # Определяем тип контента
            if path.endswith('.html'):
                content_type = 'text/html'
            elif path.endswith('.css'):
                content_type = 'text/css'
            elif path.endswith('.js'):
                content_type = 'text/javascript'
            elif path.endswith('.svg'):
                content_type = 'image/svg+xml'
            elif path.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                content_type = 'image/*'
            else:
                self.send_error(403, "Forbidden!")
                return

            # Отправляем ответ
            self.send_response(200)
            self.send_header('Content-type', content_type)
            self.end_headers()

            # Читаем и отправляем содержимое файла
            with open(full_path, 'rb') as file:
                self.wfile.write(file.read())

        except Exception as e:
            self.send_error(500, f"Internal Server Error: {str(e)}")


if __name__ == "__main__":
    hostName = "localhost"
    serverPort = 8080
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print(f"Сервер запущен по адресу http://{hostName}:{serverPort}")
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
    webServer.server_close()
    print("Сервер остановлен.")