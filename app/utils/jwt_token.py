import jwt
from datetime import datetime, timedelta, timezone


def generate_jwt_token(user_info: dict, secret_key: str) -> str:
    """
    :param user_info: 用户信息
    :param secret_key: 密钥
    :return: token
    """
    payload = {
        "user_id": user_info.get('id'),
        'user_name': user_info.get('username'),
        "exp": datetime.now(timezone.utc) + timedelta(days=7), 
        "iat": datetime.now(timezone.utc),
    }
    token = jwt.encode(payload, secret_key, algorithm="HS256")

    return token


def verify_jwt_token(token: str, secret_key: str) -> dict:
    """
    :param token: token
    :param secret_key: 密钥
    :return: payload
    """
    try:
        payload = jwt.decode(token, secret_key, algorithms=["HS256"])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    except Exception as e:
        return None
    return None



# 示例
if __name__ == '__main__':
    token = generate_jwt_token({'id': 1, 'username': 'admin'}, '123456')
    print(token)
    payload = verify_jwt_token(token, '123456')
    print(payload)

