from tests.registry import test
from strata.http.response import HTTPResponse


@test
def test_response():
    response = HTTPResponse(
        200,
        {"Content-Type": "text/plain"},
        "OK"
    )

    raw = response.to_bytes().decode()

    assert "HTTP/1.1 200 OK" in raw
    assert "Content-Length: 2" in raw