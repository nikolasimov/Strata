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
        
        request.client_address = self.client_address

        def final_handler(req):

            #Proxy
            proxy = self.router.match_proxy(req.path)
            if proxy:
                proxy_handler = ReverseProxy()
                return proxy_handler.forward(req, proxy)

            #Static
            static = StaticFileHandler()
            file_content, content_type = static.get_file(req.path)

            if file_content is not None:
                return HTTPResponse(
                    200,
                    {"Content-Type": content_type},
                    file_content
                )

            #Router
            handler = self.router.resolve(req)
            return handler(req)
        
        response = self.router.apply_middlewares(request, final_handler)

        self.client_socket.sendall(response.to_bytes())
        self.client_socket.close()