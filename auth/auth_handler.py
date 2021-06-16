import time
import jwt

from typing import Dict

JWT_SECRET = "jeffQL"
JWT_ALGORITHM = "HS256"


def create_access_token(user_id: str, expiretime: int) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + expiretime
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token.decode('ascii')


def decode_access_token(token: str) -> dict:
    try:
        decoded_token = jwt.decode(
            token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
