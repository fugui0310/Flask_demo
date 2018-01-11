from flask import Flask, render_template, request,Blueprint

from app.loginform import LoginForm
from app.sqlpool import func




account = Blueprint('account', __name__)


@account.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = LoginForm()
        return render_template('login.html', form=form)
    else:
        form = LoginForm(formdata=request.form)
        if form.validate():
            conn_db = func()
            user_tuple = tuple(form.data.values())
            for item in conn_db:
                if item[1:3] == user_tuple:
                    return render_template('index.html', )
        else:
            print(form.errors)
        return render_template('login.html', form=form)