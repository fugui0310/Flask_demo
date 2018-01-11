from flask import Flask, render_template, request,Blueprint

from app.loginform import LoginForm
from app.sqlpool import func




main = Blueprint('main', __name__)


@main.route('/index', methods=['GET', 'POST'])

def index():
    return render_template('index.html')