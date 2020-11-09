from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

class Test_Create_Profile(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(username='test_user1',password='123456789')
        test_profile = Profile.objects.create(user = testuser1)
    
    def test_profile_content(self):
        user = User.objects.get(id=1)
        profile = Profile.objects.get(id=1)

        self.assertEqual(user.username,'test_user1')
        self.assertEqual(profile.image, 'default.jpg')
        self.assertEqual(str(profile), 'test_user1 Profile')

