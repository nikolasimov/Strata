from strata.http.request import HTTPRequest


def test_request():
    req = HTTPRequest("GET", "/", "HTTP/1.1", {"Host": "localhost"})

    assert req.method == "GET"
    assert req.path == "/"
    assert req.version == "HTTP/1.1"
    assert req.headers["Host"] == "localhost"


if __name__ == "__main__":
    test_request()
    print("request test passed")