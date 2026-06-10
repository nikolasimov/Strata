from strata.http.middleware.base import Middleware
from strata.logging import logger


class LoggerMiddleware(Middleware):
    def process(self, request, next_handler):
        response = next_handler(request)

        status = getattr(response, "status_code", "???")

        logger.info(
            f"{request.client_address[0]} "
            f"{request.method} "
            f"{request.path} "
            f"-> {status}"
        )

        return response