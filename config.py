import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
WTF_CSRF_ENABLED = True
SECRET_KEY = 'Iwrotethisinvimsoitcanbeassumedtobepseudorandom'

OPENID_PROVIDERS = [
        {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'}
        ]
