from flask import Blueprint, request
from models import db, User

user = Blueprint('user', __name__)

@user.route('/account/login', methods=['POST'])
def add_user():
    username = request.json.get('username')
    email = request.json.get('email')
    new_user = User(username=username, email=email)
    db.session.add(new_user)
    db.session.commit()
    return {'message': f'User {username} added!'}, 201

@user.route('/account/register', methods=['GET'])
def get_users():
    users = User.query.all()
    return {'users': [user.username for user in users]}, 200
