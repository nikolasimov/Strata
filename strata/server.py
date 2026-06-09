import socket
from strata.connection import Connection

class Server:
    def __init__(self, router, host: str = "127.0.0.1", port: int = 8080, backlog: int = 5):
        self.router = router
        self.host = host
        self.port = port
        self.backlog = backlog
        
        self.server_socket = None
        self.is_running = False
        
    def _setup_socket(self):
        #AF_INET -> IPv4 Network
        #SOCK_STREAM -> TCP
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        #allows the server to reuse the port immediatly after restarting
        self.server_socket.setsockopt(
            socket.SOL_SOCKET,
            socket.SO_REUSEADDR,
            1,
        )
        
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(self.backlog)
        
        print(f"[Strata] listening on http://{self.host}:{self.port}")
        
    def start(self):
        self._setup_socket()
        self.is_running = True
        
        try:
            while self.is_running:
                client_socket, client_address = self.server_socket.accept()
                print(f"[Strata] connection from {client_address}")
                
                connection = Connection(client_socket, client_address, self.router)
                connection.handle()
                
        except KeyboardInterrupt:
            print("\n [Strata] Shutting down server...")
        finally:
            self.stop()
            
    def stop(self):
        self.is_running = False
        
        if self.server_socket:
            self.server_socket.close()
            self.server_socket = None
            
        print("[Strata] Server stopped.")