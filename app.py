from flask import request, render_template, redirect, make_response

from loader import app, db


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)