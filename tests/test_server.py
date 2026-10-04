import unittest
import threading
import json
from http.server import HTTPServer
from urllib.request import urlopen

from src.server import Handler


class TestServer(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(("127.0.0.1", 0), Handler)
        cls.port = cls.server.server_address[1]

        cls.thread = threading.Thread(
            target=cls.server.serve_forever
        )
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.thread.join()

    def test_root(self):
        response = urlopen(f"http://127.0.0.1:{self.port}/")
        self.assertEqual(response.status, 200)

    def test_healthz(self):
        response = urlopen(f"http://127.0.0.1:{self.port}/healthz")
        self.assertEqual(response.status, 200)

        body = response.read().decode()
        self.assertTrue(len(body) > 0)

    def test_tasks(self):
        response = urlopen(f"http://127.0.0.1:{self.port}/tasks")
        self.assertEqual(response.status, 200)

        data = json.loads(response.read().decode())
        self.assertEqual(len(data), 3)


if __name__ == "__main__":
    unittest.main()