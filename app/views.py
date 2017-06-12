from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Sofus'}
    posts = [
            {
                'author': {'nickname': 'Thierry Lacour'},
                'body' : 'Random Pokémon Rant'
                },
            {
                'author': {'nickname': 'Sofus'},
                'body' : 'Kids need to learn online behaviour'
                }
            ]

    return render_template('index.html',
            title='CoDeAcademy',
            user=user,
            posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                title='Sign In',
                form= form)
