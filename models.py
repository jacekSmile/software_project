from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    uid = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='用户ID')
    username = db.Column(db.String(50), unique=True, nullable=False, comment='用户账号')
    password = db.Column(db.String(255), nullable=False, comment='用户密码')
    nickname = db.Column(db.String(32), unique=True, nullable=False, comment='用户昵称')
    avatar = db.Column(db.String(500), nullable=True, comment='用户头像url')
    background = db.Column(db.String(500), nullable=True, comment='主页背景图url')
    gender = db.Column(db.SmallInteger, nullable=False, default=2, comment='性别 0女 1男 2未知')
    description = db.Column(db.String(100), nullable=True, comment='个性签名')
    exp = db.Column(db.Integer, nullable=False, default=0, comment='经验值')
    coin = db.Column(db.Float, nullable=False, default=0.0, comment='硬币数')
    vip = db.Column(db.SmallInteger, nullable=False, default=0, comment='会员类型 0普通用户 1月度大会员 2季度大会员 3年度大会员')
    state = db.Column(db.SmallInteger, nullable=False, default=0, comment='状态 0正常 1封禁 2注销')
    role = db.Column(db.SmallInteger, nullable=False, default=0, comment='角色类型 0普通用户 1管理员 2超级管理员')
    auth = db.Column(db.SmallInteger, nullable=False, default=0, comment='官方认证 0普通用户 1个人认证 2机构认证')
    auth_msg = db.Column(db.String(30), nullable=True, comment='认证说明')
    create_date = db.Column(db.DateTime, nullable=False, comment='创建时间')
    delete_date = db.Column(db.DateTime, nullable=True, comment='注销时间')

    def __repr__(self):
        return f'<User {self.username}>'