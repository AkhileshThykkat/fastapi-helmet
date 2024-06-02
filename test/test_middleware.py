from fastapi.testclient import TestClient
from fastapi import FastAPI
from fastapi_helmet.middleware import HelmetMiddleware

app = FastAPI()
app.add_middleware(HelmetMiddleware)

client = TestClient(app)


def test_security_headers():
    response = client.get("/")
    assert response.headers["X-Content-Type-Options"] == "nosniff"
    assert response.headers["X-Frame-Options"] == "DENY"
    assert response.headers["X-XSS-Protection"] == "1; mode=block"
    assert response.headers["Referrer-Policy"] == "no-referrer"
    assert response.headers["Content-Security-Policy"] == "default-src 'self'"
    assert (
        response.headers["Strict-Transport-Security"]
        == "max-age=63072000; includeSubDomains"
    )
    assert response.headers["Expect-CT"] == "max-age=86400, enforce"
