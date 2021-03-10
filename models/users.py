from config import db


class Users(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

    def __repr__(self):
        return '<User %r>' % self.username
