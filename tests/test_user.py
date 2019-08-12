import unittest
from app.models import *

def setUp(self):
        """
        Will be called before every test
        """

        db.create_all()

        # create test admin user
        admin = User(author="admin", password="sly14", is_admin=True)

        # create test non-admin user
        hustler = User(author="test_user", password="slytest")

        # save users to database
        db.session.add(admin)
        db.session.add(hustler)
        db.session.commit()

def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'cossie')

    def test_password_setter(self):
        self.assertTrue(self.new_user.password_hash is not None)

    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('cossie'))

class CommentsModelTest(unittest.TestCase):

    def setUp(self):
       self.new_comment = Comments(id=1, user_id = 2, comment = 'cross buns',blogs_id = '5',date_posted='2019-10-08')

    def test_comment_variables(self):

       # self.assertEquals(self.new_comment.id, 2)
       self.assertEquals(self.new_comment.comment,'cross buns')
       self.assertEquals(self.new_comment.date_posted,'2019-10-08')
       self.assertEquals(self.new_comment.user_id, 2)
       # self.assertEquals(self.new_comment.blogs_id, 4)

    def test_save_comment(self):

        self.assertTrue(len(Comments.query.all())>0)

class BlogsModelTest(unittest.TestCase):

    def test_save_blog(self):
        self.assertTrue(len(Blogs.query.all())>0)


class SubscriberModelTest(unittest.TestCase):

    def setUp(self):
        self.new_subscriber = Subscriber(id = 1 , name = 'sly', email = 'sly@gmail.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_subscriber,Subscriber))

    def test_variables(self):
        self.assertEquals(self.new_subscriber.id, 1)
        self.assertEquals(self.new_subscriber.name, 'sly')
        self.assertEquals(self.new_subscriber.email, 'sly@gmail.com')
