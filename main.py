from strata.server import Server
from strata.http.router import HTTPRouter
from strata.config import Config


config = Config()
router = HTTPRouter()

# -------------------------
# Example routes
# -------------------------
def home(request):
    from strata.http.response import HTTPResponse
    return HTTPResponse(200, {"Content-Type": "text/plain"}, "Welcome to Strata")


def hello(request):
    from strata.http.response import HTTPResponse
    return HTTPResponse(200, {"Content-Type": "text/plain"}, "Hello from Strata")


router.add("GET", "/", home)
router.add("GET", "/hello", hello)

# -------------------------
# Load proxies from config
# -------------------------
for path, target in config.data.get("proxy", {}).items():
    router.add_proxy(path, target)

# -------------------------
# Start server
# -------------------------
server = Server(router=router)

try:
    server.start()
except KeyboardInterrupt:
    server.stop()