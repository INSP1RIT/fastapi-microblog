from fastapi_users.authentication import JWTStrategy, AuthenticationBackend
from fastapi_users.authentication import CookieTransport

cookie_transport = CookieTransport(cookie_name="blog", cookie_max_age=3600)

SECRET = "fdskfl42irdfisskam12"


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
