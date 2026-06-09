from strata.server import Server
from strata.http.router import HTTPRouter
from strata.http.response import HTTPResponse


router = HTTPRouter()


def home(request):
    return HTTPResponse(
        status_code=200,
        headers={"Content-Type": "text/plain"},
        body="Welcome to Strata\n",
    )


def hello(request):
    return HTTPResponse(
        status_code=200,
        headers={"Content-Type": "text/plain"},
        body="Hello from Strata\n",
    )


router.add("GET", "/", home)
router.add("GET", "/hello", hello)


server = Server(router=router)

try:
    server.start()
except KeyboardInterrupt:
    server.stop()