from strata.http.static import StaticFileHandler
from strata.http.response import HTTPResponse
from strata.http.parser import HTTPParser
from strata.http.proxy import ReverseProxy


class Connection:
    def __init__(self, client_socket, client_address, router):
        self.client_socket = client_socket
        self.client_address = client_address
        self.router = router

    def handle(self):
        data = self.client_socket.recv(1024)

        parser = HTTPParser()
        request = parser.parse(data)

        #PROXY
        proxy = self.router.match_proxy(request.path)
        if proxy:
            proxy_handler = ReverseProxy()
            raw_response = proxy_handler.forward(request, proxy)

            self.client_socket.sendall(raw_response)
            self.client_socket.close()
            return

        #STATIC
        static = StaticFileHandler()
        file_content, content_type = static.get_file(request.path)

        if file_content is not None:
            response = HTTPResponse(
                200,
                {"Content-Type": content_type},
                file_content
            )
            self.client_socket.sendall(response.to_bytes())
            self.client_socket.close()
            return

        #ROUTER
        handler = self.router.resolve(request)
        response = handler(request)

        if response is None:
            response = HTTPResponse(
                500,
                {"Content-Type": "text/plain"},
                "Handler returned no response"
            )

        self.client_socket.sendall(response.to_bytes())
        self.client_socket.close()