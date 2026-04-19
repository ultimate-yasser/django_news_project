from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.


class UsersManagersTests(TestCase):
    def test_create_user(self):
        user = get_user_model().objects.create_user(
            username="testuser",
            email="testemail@gmail.com",
            password="testpass123",
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testemail@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            username="testsuperuser",
            email="superemail@gmail.com",
            password="superpass123",
        )
        self.assertEqual(user.username, "testsuperuser")
        self.assertEqual(user.email, "superemail@gmail.com")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
