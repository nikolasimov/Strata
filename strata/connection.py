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

            handler = self.router.resolve(request)
            response = handler(request)

            self.client_socket.sendall(response.to_bytes())
            self.client_socket.close()