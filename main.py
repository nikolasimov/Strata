from strata.server import Server
from strata.http.router import HTTPRouter
from strata.http.response import HTTPResponse


router = HTTPRouter()


def home(request):
    return HTTPResponse(
        200,
        {"Content-Type": "text/html"},
        """
        <html>
            <head><title>Strata</title></head>
            <body>
                <h1>Welcome to Strata</h1>
                <p>This is my first web server</p>
            </body>
        </html>
        """
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