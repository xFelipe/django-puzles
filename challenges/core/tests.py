from django.test import TestCase


# Create your tests here.
class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_status(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response, 'home.html')

    def test_title(self):
        self.assertContains(self.response, '<title>Exercícios feitos no Django</title>')
