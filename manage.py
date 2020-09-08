from flask import jsonify
import os
from dotenv import load_dotenv
from config import create_app

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

app = create_app(os.getenv('FLASK_CONFIG') or 'default')


@app.route('/')
def entry_point():
    return jsonify({'endpoint': '/'})


@app.route('/test')
def test():
    from utils.pdbc import PDBC
    pdbc = PDBC()
    pdbc.setup()
    pdbc.add()

    from models.user import User
    o = User.query.all()
    print(o)
    return jsonify({'endpoint': '/'})
