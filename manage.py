import os

from dotenv import load_dotenv

from config import create_api, create_app, scheduler
from utils.handle import handle_success

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
api = create_api(app)


@app.route('/')
def root_path():
    return handle_success()


@scheduler.task('interval', id='do_job_1', seconds=5, misfire_grace_time=900)
def job1():
    print('Job 1 executed')
