from django.test import TestCase

class HomeTestCase(TestCase):
    def test_can_access_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)