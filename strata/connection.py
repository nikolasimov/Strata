from strata.http.static import StaticFileHandler
from strata.http.response import HTTPResponse
from strata.http.parser import HTTPParser


class Connection:
    def __init__(self, client_socket, client_address, router):
        self.client_socket = client_socket
        self.client_address = client_address
        self.router = router

    def handle(self):
        data = self.client_socket.recv(1024)

        parser = HTTPParser()
        request = parser.parse(data)

        static = StaticFileHandler()

        file_content, content_type = static.get_file(request.path)
        
        if file_content:
            response = HTTPResponse(
                200,
                {"Content-Type": content_type},
                file_content
            )
            self.client_socket.sendall(response.to_bytes())
            self.client_socket.close()
            return

        handler = self.router.resolve(request)
        response = handler(request)

        self.client_socket.sendall(response.to_bytes())
        self.client_socket.close()