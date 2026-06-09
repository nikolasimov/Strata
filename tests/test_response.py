from strata.http.response import HTTPResponse


def test_response():
    response = HTTPResponse(
        200,
        {"Content-Type": "text/plain"},
        "OK"
    )

    raw = response.to_bytes().decode()

    assert "HTTP/1.1 200 OK" in raw
    assert "Content-Type: text/plain" in raw
    assert "Content-Length: 2" in raw
    assert "\r\n\r\nOK" in raw


if __name__ == "__main__":
    test_response()
    print("response test passed")