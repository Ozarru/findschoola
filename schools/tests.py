from django.test import TestCase
from .models import School
from accounts.models import CustomUser

# Create your tests here.
print('testing school, 1, 2')

testUser = CustomUser(
    username='TestSchool',
    email='test@school.com',
    first_name='TestSchool',
    last_name='TestSchool',
    password='TestSchool',
    role='gestionaire',
    subrole='school-admin',

)


class ModelTesting(TestCase):

    def setUp(self):
        self.school = School.objects.create(
            # manager=testUser,
            name='TestSchool',
            website='TestSchool',
            address='TestSchool',
            tel='TestSchool',
            cel='TestSchool',
            moto='TestSchool',
            year_founded='TestSchool',

        )

    def school_test(self):
        data = self.school
        self.assertTrue(isinstance(data, School))
        self.assertEqual(str(data), self.school.name)
