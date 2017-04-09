from app import app 
from flask import render_template, flash, redirect
from forms import LoginForm
@app.route('/') 
@app.route('/index') 
def index():
    user = {'nickname': 'qill'}
    posts = [
        {
            'author': {'nickname': 'john'},
            'atitle': {'body': 'beautiful day in poland!'}
        },
        {
            'author': {'nickname': 'David'},
            'atitle': {'body': 'Nice shoot!'}
        }
    ]
    return render_template('index.html', titile='home', user=user, posts=posts)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('"Login requested for OpenID="' + form.openid.data + '", rember_me='
              + str(form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In',
    form=form, providers=app.config['OPENID_PROVIDERS'])