from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
# Create your tests here.

class CreateUserTest(APITestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser('prueba_admin', 'prueba@admin.com', 'pruebapassword')
        self.client.login(username='prueba_admin', password = 'pruebapassword')
        self.data = {'username': 'maitebu', 'first_name': 'maite', 'last_name': 'butron'}
    
    def test_can_create_user(self):
        response = self.client.post(reverse('user-list'), self.data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)