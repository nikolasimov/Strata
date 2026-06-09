class HTTPRouter:
    VALID_METHODS = ("GET", "POST", "PUT", "PATCH", "DELETE")

    def __init__(self):
        self.routes = {}
        self.proxy_routes = {}

    def add(self, method, path, handler):
        method = method.upper()

        if method not in self.VALID_METHODS:
            raise ValueError(f"Unsupported HTTP method: {method}")

        if not path or not path.startswith("/"):
            raise ValueError("Path must start with '/'")

        if not callable(handler):
            raise ValueError("Handler must be callable")

        route_key = (method, path)

        if route_key in self.routes:
            raise RuntimeError(
                f"Route {method} {path} is already registered"
            )

        self.routes[route_key] = handler

    def resolve(self, request):
        route_key = (request.method, request.path)
        return self.routes.get(route_key, self.not_found)

    def not_found(self, request):
        from strata.http.response import HTTPResponse

        return HTTPResponse(
            status_code=404,
            headers={"Content-Type": "text/plain"},
            body=f"404 Not Found\n",
        )
    
    def add_proxy(self, path_prefix, target_url):
        self.proxy_routes[path_prefix] = target_url
        
    def match_proxy(self, path):
        for prefix, target in self.proxy_routes.items():
            if path.startswith(prefix):
                return target
        return None