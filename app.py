from flask import Flask
from flask_migrate import Migrate
from models import db
from routes.user import user as user_blueprint


def create_app():
    app = Flask(__name__)

    # 设置 config
    app.config.from_object('config.Config')
    # 注册蓝图
    app.register_blueprint(user_blueprint, url_prefix='/user')
    
    # Initialize the database with the app
    db.init_app(app)
    
    migrate = Migrate(app, db)
    Migrate(app, db)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
