from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Sofus'}
    posts = [
            {
                'author': {'nickname': 'Thierry'},
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
