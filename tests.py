from datetime import datetime, timedelta
import unittest
from app import app, db
from app.models import User, Post


class UserModelCase(unittest.TestCase):
    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        app_ctxt = app.app_context()
        app_ctxt.push()
        db.create_all()
        app_ctxt.pop()

    def tearDown(self):
        app_ctxt = app.app_context()
        app_ctxt.push()
        db.session.remove()
        db.drop_all()
        app_ctxt.pop()

    def test_password_hashing(self):
        app_ctxt = app.app_context()
        app_ctxt.push()
        u = User(username='susan')
        u.set_password('cat')
        self.assertFalse(u.check_password('dog'))
        self.assertTrue(u.check_password('cat'))
        app_ctxt.pop()

    def test_avatar(self):
        app_ctxt = app.app_context()
        app_ctxt.push()
        u = User(username='john', email='john@example.com')
        self.assertEqual(
            u.avatar(128),
            ('https://www.gravatar.com/avatar/'
            'd4c74594d841139328695756648b6bd6'
            '?d=identicon&s=128'))
        app_ctxt.pop()

    def test_follow(self):
        app_ctxt = app.app_context()
        app_ctxt.push()
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='susan', email='susan@example.com')
        db.session.add(u1)
        db.session.add(u2)
        db.session.commit()
        self.assertEqual(u1.followed.all(), [])
        self.assertEqual(u2.followers.all(), [])

        u1.follow(u2)
        db.session.commit()
        self.assertTrue(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 1)
        self.assertEqual(u2.followers.count(), 1)

        u1.unfollow(u2)
        db.session.commit()
        self.assertFalse(u1.is_following(u2))
        self.assertEqual(u1.followed.count(), 0)
        self.assertEqual(u2.followers.count(), 0)
        app_ctxt.pop()

    def test_follow_posts(self):
        app_ctxt = app.app_context()
        app_ctxt.push()
        u1 = User(username='john', email='john@example.com')
        u2 = User(username='susan', email='susan@example.com')
        u3 = User(username='mary', email='mary@example.com')
        u4 = User(username='david', email='david@example.com')
        db.session.add_all([u1, u2, u3, u4])

        now = datetime.utcnow()
        p1 = Post(
            body='post from john', author=u1,
            timestamp=now + timedelta(seconds=1)
        )
        p2 = Post(
            body='post from susan', author=u2,
            timestamp=now + timedelta(seconds=4)
        )
        p3 = Post(
            body='post from mary', author=u3,
            timestamp=now + timedelta(seconds=3)
        )
        p4 = Post(
            body='post from david', author=u4,
            timestamp=now + timedelta(seconds=2)
        )
        db.session.add_all([p1, p2, p3, p4])
        db.session.commit()

        u1.follow(u2)
        u1.follow(u4)
        u2.follow(u3)
        u3.follow(u4)
        db.session.commit()

        f1 = u1.followed_posts().all()
        f2 = u2.followed_posts().all()
        f3 = u3.followed_posts().all()
        f4 = u4.followed_posts().all()
        self.assertEqual(f1, [p2, p4, p1])
        self.assertEqual(f2, [p2, p3])
        self.assertEqual(f3, [p3, p4])
        self.assertEqual(f4, [p4])
        app_ctxt.pop()


if __name__ == "__main__":
    unittest.main(verbosity=2)
