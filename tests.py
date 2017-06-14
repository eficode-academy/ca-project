#!flask/bin/python
import os
import unittest
from datetime import datetime
from config import basedir
from app import app, db
from app.models import Post

class TestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_silly(self):
        assert True
    
    def test_add_post_is_added(self):
        post = Post(title='test1', user_name='test1', body='test1', timestamp=datetime.utcnow())
        db.session.add(post)
        db.session.commit()
        print(len(Post.query.all()))
        number_of_posts = len(Post.query.all())
        self.assertEqual(number_of_posts,1)

if __name__ == '__main__':
    unittest.main()
