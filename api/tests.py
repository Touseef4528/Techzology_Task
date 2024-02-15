from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login(self):
        client = Client()
        response = client.post(reverse('login'), {'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertTrue('_auth_user_id' in client.session)

    def test_unauthorized_access(self):
        client = Client()
        response = client.get(reverse('protected_endpoint'))
        self.assertEqual(response.status_code, 403)
