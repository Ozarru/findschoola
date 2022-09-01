from django.test import TestCase
from .models import CustomUser

# Create your tests here.
print('testing user, 1, 2')


class ModelTesting(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(
            username='TestSchool',
            email='test@school.com',
            first_name='TestSchool',
            last_name='TestSchool',
            password='TestSchool',
            role='gestionaire',
            subrole='school-admin',

        )

    def user_test(self):
        data = self.user
        self.assertTrue(isinstance(data, CustomUser))
        self.assertEqual(str(data), 'TestSchool')
