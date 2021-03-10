from config import db
from models.users import Users
from flask_restful import Resource, reqparse, fields, marshal_with
from utils.handle import handle_success, handle_error

parser = reqparse.RequestParser()
parser.add_argument('username')
parser.add_argument('email')


class User(Resource):
    def get(self, user_id):
        user = Users.query.filter_by(id=user_id).first()
        if user is None:
            return handle_error(message="User {} doesn't exist".format(user_id), code='10404')
        return handle_success(message='query success', data=user.to_json())

    def delete(self, user_id):
        user = Users.query.filter_by(id=user_id).first()
        if user is None:
            return handle_error(message="User {} doesn't exist".format(user_id), code='10404')
        db.session.delete(user)
        db.session.commit()
        db.session.remove()
        return handle_success(message='delete success', code='10204')

    def put(self, user_id):
        args = parser.parse_args()
        user = Users.query.filter_by(id=user_id).first()
        user.username = args.username
        user.email = args.email
        data = user.to_json()
        db.session.commit()
        db.session.remove()
        return handle_success(message='update success', code='10204',data=data)


class UserList(Resource):
    def get(self):
        query = Users.query.all()
        list = [o.to_json() for o in query]
        return handle_success(message='query success', data=list)

    def post(self):
        args = parser.parse_args()
        user = Users(username=args.username, email=args.email)
        db.session.add(user)
        db.session.commit()
        db.session.remove()
        return handle_success(message='add success', code='10201')
