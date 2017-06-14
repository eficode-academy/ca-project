import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Setup out SQLITE database connection
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# Do cross site request forgery protection
WTF_CSRF_ENABLED = True
SECRET_KEY = 'Iwrotethisinvimsoitcanbeassumedtobepseudorandom'
