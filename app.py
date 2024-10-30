from flask import Flask
from dotenv import load_dotenv
from routes.user import user as user_blueprint

load_dotenv()

def create_app():
    app = Flask(__name__)

    # 注册蓝图
    app.register_blueprint(user_blueprint, url_prefix='/user')

    return app

app = create_app()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
