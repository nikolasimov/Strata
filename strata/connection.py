from http.parser import HTTPParser

class Connection:
    def __init__(self, client_socket,client_address):
        self.client_socket = client_socket
        self.client_address = client_address
        
    def handle(self):
        data = self.client_socket.recv(1024)
        
        parser = HTTPParser()
        request = parser.parse(data)
        
        print(request.method, request.path)
        
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/plain\r\n"
            "Content-Length: 2\r\n"
            "\r\n"
            "OK"
        )



        self.client_socket.sendall(response.encode())
        
        
        
        
        
        self.client_socket.close()