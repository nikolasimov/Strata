from .base import Middleware

class LoggerMiddleware(Middleware):
    def process(self, request, next_handler):
        print(f"[Strata] {request.method} {request.path}")

        response = next_handler(request)

        print(f"[Strata] done")

        return response