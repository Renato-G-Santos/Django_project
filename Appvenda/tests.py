from django.test import TestCase, Client

# Create your tests here.

class TestarRespose_200(TestCase):
    def test_verificar_html(self):
        client = Client()
        response = client.get('/produtos/')
        self.assertTemplateUsed(response, 'exibir.html' )
