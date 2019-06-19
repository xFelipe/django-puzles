from django.test import TestCase


# Create your tests here.
class TestDiamonds(TestCase):
    def setUp(self):
        self.response = self.client.get('/diamonds/')

    def testStatus(self):
        self.assertEqual(200, self.response.status_code)

    def testTemplate(self):
        self.assertTemplateUsed(self.response, 'diamonds/diamonds_form.html')
