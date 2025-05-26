from flask import session


class AuthCookie:
    def __init__(self, user_info: dict = None):
        self.user_info = user_info 
    
    def login_user(self) -> None:
        session.permanent = True  # 设置会话为永久有效
        for key, value in self.user_info.items():
            session[key] = value


    def logout_user(self) -> None:
        session.clear()


    def get_user_info(key: str) -> str:
        return session.get(key, None)


    def clear_auth_cookie() -> None:
        session.pop('user_id', None)

    def is_login(self, user_id: str = None) -> bool:
        return user_id in session

    def admin_required():
        pass

    def login_required():
        pass
