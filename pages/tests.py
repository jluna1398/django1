from django.test import TestCase, SimpleTestCase


class PagesTest(SimpleTestCase):
    def test_url_exist(self):
        resource = self.client.get('/')
        self.assertEqual(resource.status_code, 200)



# Create your tests here.
