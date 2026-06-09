from tests.registry import test
from strata.http.parser import HTTPParser


@test
def test_parser():
    raw = b"GET /hello HTTP/1.1\r\nHost: localhost\r\n\r\n"

    parser = HTTPParser()
    request = parser.parse(raw)

    assert request.method == "GET"
    assert request.path == "/hello"