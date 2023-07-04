import uuid

from fastapi_users import FastAPIUsers

from .manager import get_user_manager
from .models import User
from .strategy import auth_backend

fastapi_users = FastAPIUsers[User, uuid.UUID](
    get_user_manager,
    [auth_backend],
)
