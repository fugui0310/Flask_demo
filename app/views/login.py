from flask import render_template, request, Blueprint,current_app,redirect

from app.utils.loginform import LoginForm
from app.utils.sqlpool import SQLHelper

account = Blueprint('account', __name__)


@account.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = LoginForm()
        return render_template('login.html', form=form)
    else:
        form = LoginForm(formdata=request.form)
        if form.validate():
            with SQLHelper() as helper:
                result = helper.fetchone('select * from user where user=%s and password = %s',
                                         [request.form.get('user'), request.form.get('password'), ])
            if result:
                current_app.auth_manager.login(result['user'])
                return redirect('/index', )
        return render_template('login.html', form=form)