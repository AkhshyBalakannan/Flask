import unittest

from run import app


def login(client, username, password):
    """Start with a login request."""
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)


def logout(client):
    return client.get('/logout', follow_redirects=True)


class FlaskTest(unittest.TestCase):

    def test_base_route(self):
        """Start with a blank database."""
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertEqual(response.status_code, 200)

    def test_login_logout(self):
        """Make sure login and logout works."""

        client = app.test_client(self)
        username = app.config["USERNAME"]
        password = app.config["PASSWORD"]

        rv = login(client, username, password)
        self.assertEqual(b'You were logged in', rv)

        rv = logout(client)
        self.assertEqual(b'You were logged out', rv.data)

        rv = login(client, f"{username}x", password)
        self.assertEqual(b'Invalid username', rv.data)

        rv = login(client, username, f'{password}x')
        self.assertEqual(b'Invalid password', rv.data)


if __name__ == "__main__":
    unittest.main()
