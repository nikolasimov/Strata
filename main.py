from strata.server import Server
from strata.http.router import HTTPRouter

from strata.http.middleware.logger import LoggerMiddleware
from strata.http.middleware.headers import HeaderMiddleware


router = HTTPRouter()

router.use(LoggerMiddleware())
router.use(HeaderMiddleware())

server = Server(router=router)

try:
    server.start()
except KeyboardInterrupt:
    server.stop()