
class HTTPResponse:
    def __init__(self, status_code=200, headers=None, body=""):
        self.status_code = status_code
        self.headers = headers or {}
        self.body = body
    
    def to_bytes(self):
        body = self.body.encode("utf-8") if isinstance(self.body, str) else self.body

        self.headers["Content-Length"] = str(len(body))

        status_line = f"HTTP/1.1 {self.status_code} OK\r\n"

        headers = ""
        for key, value in self.headers.items():
            headers += f"{key}: {value}\r\n"

        response = status_line + headers + "\r\n"

        return response.encode("utf-8") + body