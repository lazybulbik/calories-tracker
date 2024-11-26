from flask import request, render_template, redirect, make_response

from loader import app, get_db

from api import auth


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)