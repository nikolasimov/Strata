import socket


class ReverseProxy:
    def forward(self, request, target_url):
        raw_request = self._build_request(request)

        host, port = self._parse_target(target_url)

        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        client.sendall(raw_request)

        response = self._receive_response(client)
        client.close()

        return response

    def _build_request(self, request):
        request_line = f"{request.method} {request.path} HTTP/1.1\r\n"

        headers = ""
        for k, v in request.headers.items():
            headers += f"{k}: {v}\r\n"

        headers += "\r\n"

        return (request_line + headers).encode("utf-8")

    def _parse_target(self, url):
        # simple version: http://127.0.0.1:5000
        url = url.replace("http://", "")
        host, port = url.split(":")
        return host, int(port)

    def _receive_response(self, client):
        return client.recv(4096)