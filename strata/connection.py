from strata.http.parser import HTTPParser
from strata.http.response import HTTPResponse

class Connection:
    def __init__(self, client_socket,client_address):
        self.client_socket = client_socket
        self.client_address = client_address
        
    def handle(self):
        data = self.client_socket.recv(1024)
        
        parser = HTTPParser()
        request = parser.parse(data)
        
        print(request.method, request.path)
        
        response = HTTPResponse(
            200, 
            {"Content-Type": "text/plain"},
            "OK"
        )
        
        
        self.client_socket.sendall(response.to_bytes())
        self.client_socket.close()