from tests.registry import test
from strata.http.router import HTTPRouter
from strata.http.response import HTTPResponse


@test
def test_router_add_and_resolve():
    router = HTTPRouter()

    def home(request):
        return HTTPResponse(200, {}, "home")

    router.add("GET", "/", home)

    request = type("Request", (), {"method": "GET", "path": "/"})()

    handler = router.resolve(request)

    assert handler == home


@test
def test_router_handler_execution():
    router = HTTPRouter()

    def hello(request):
        return HTTPResponse(200, {}, "hello")

    router.add("GET", "/hello", hello)

    request = type("Request", (), {"method": "GET", "path": "/hello"})()

    handler = router.resolve(request)
    response = handler(request)

    assert isinstance(response, HTTPResponse)
    assert response.body == "hello"


@test
def test_router_not_found():
    router = HTTPRouter()

    request = type("Request", (), {"method": "GET", "path": "/missing"})()

    handler = router.resolve(request)
    response = handler(request)

    assert isinstance(response, HTTPResponse)
    assert response.status_code == 404