from flask import Flask, g
from database import Database

from config import SECRET_KEY

app = Flask(__name__)

def get_db():
    if 'db' not in g:
        g.db = Database('db/db.db')
    return g.db

@app.teardown_appcontext
def close_db(error):
    db = g.pop('db', None)
    if db is not None:
        del db

app.config['SECRET_KEY'] = SECRET_KEY

