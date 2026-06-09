from strata.http.parser import HTTPParser


def test_parser():
    raw = b"GET /hello HTTP/1.1\r\nHost: localhost\r\n\r\n"

    parser = HTTPParser()
    request = parser.parse(raw)

    assert request.method == "GET"
    assert request.path == "/hello"
    assert request.version == "HTTP/1.1"
    assert request.headers["Host"] == "localhost"


if __name__ == "__main__":
    test_parser()
    print("parser test passed")