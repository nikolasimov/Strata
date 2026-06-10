from .base import Middleware

class HeaderMiddleware(Middleware):
    def process(self, request, next_handler):
        response = next_handler(request)

        response.headers["X-Powered-By"] = "Strata"

        return response