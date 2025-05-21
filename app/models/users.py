
import enum
from sqlalchemy import Numeric


from app import db

class User(db.Model):
    __tablename__ = 'users'

    class Role(enum.Enum):
        ADMIN = '管理员'
        USER = '普通用户'
        GUEST = '游客'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True, comment='用户名')
    password = db.Column(db.String(500), nullable=False, comment='密码')
    salt = db.Column(db.String(500), nullable=False, comment='盐')
    role = db.Column(db.Enum(Role), nullable=False, comment='角色')
    avatar = db.Column(db.String(500), nullable=False, comment='头像')
    balance = db.Column(Numeric(10, 6), nullable=False, default=0, comment='余额')
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), comment='创建时间')
    updated_at = db.Column(db.DateTime, nullable=False, default=db.func.now(), onupdate=db.func.now(), comment='更新时间')

    def base_info(self):
        return {
            'id': self.id,
            'username': self.username,
            'role': self.role.value,
            'avatar': self.avatar,
            'balance': self.balance,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }