class Middleware:
    def process(self, request, next_handler):
        return next_handler(request)