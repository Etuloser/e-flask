from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def entry_point():
    return jsonify({'endpoint': '/'})
