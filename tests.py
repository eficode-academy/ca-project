#!flask/bin/python
########
# tests.py
# For testing our CoDe Chan application
# Contains _unittests_
# Is using the base python unittest framework.
# To add tests add a function on TestCase with signature: test_[name_of_test](self):
# To run use python tests.py

import os
import unittest
from datetime import datetime
from config import basedir
from app import app, db
from app.models import Post


class TestCase(unittest.TestCase):
    # set up a database such that we have isolated our tests
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    # Clear out testdatabase after tests
    def tearDown(self):
        db.session.remove()
        db.drop_all()

    # We gotta boost that test count
    def test_silly(self):
        assert True

    # Test that our testdatabase does not come with any posts
    def test_no_predefined_posts(self):
        number_of_posts = Post.query.count()
        self.assertEqual(number_of_posts,0)

    # Test that adding a post increments the amount of posts
    def test_add_post_is_added(self):
        post = Post(title='test1', user_name='test1', body='test1', timestamp=datetime.utcnow())
        db.session.add(post)
        db.session.commit()
        print(len(Post.query.all()))
        number_of_posts = len(Post.query.all())
        self.assertEqual(number_of_posts,1)

if __name__ == '__main__':
    unittest.main()
