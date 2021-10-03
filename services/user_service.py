import config
from auth import auth_handler


def user_login(name):

    access_token = auth_handler.create_access_token(
        user_id=name, expiretime=config.auth_expiretime
    )

    return {"id": 1, "name": name, "token": access_token}
