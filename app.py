from flask import request, render_template, redirect, make_response

from loader import app, get_db

from api import check_token, auth, register_module, profile, add_module


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/plan')
def plan():
    return render_template('plan.html')


@app.route('/meal_time')
def meal_time():
    return render_template('meal_time.html', meal=request.args.get('meal'))


@app.route('/add_food')
def add_food():
    return render_template('add_food.html', meal=request.args.get('meal'))


if __name__ == '__main__':
    app.run(port=5000, debug=True)