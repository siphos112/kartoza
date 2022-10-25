from django.test import TestCase
from django.contrib.auth.models import User
from users.models import UserProfile

class UserAccountTests(TestCase):
    '''
    Test class for user creation. Ran out of time...would have done more
    '''
    def test_new_superuser(self):
        super_user = User.objects.create_superuser(username='superadmin', email='supertest@test.com',
                        password='th1sp@ssw0rd4U')
        self.assertEqual(super_user.email, 'supertest@test.com')
        self.assertEqual(super_user.username, 'superadmin')
        self.assertTrue(super_user.is_superuser)
        self.assertTrue(super_user.is_staff)

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                username='trialadminuser', email='', password='thisIs@p@ssWord', is_superuser=False
            )

    def test_new_user(self):
        user = User.objects.create_user(
            username='vince.michaels@test.com', first_name='Vince', last_name='Michaels', password='p@ssword334'
        )
        self.assertEqual(user.username, 'vince.michaels@test.com')
        self.assertEqual(user.first_name, 'Vince')
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)

        with self.assertRaises(ValueError):
            User.objects.create_user(
                first_name='test', username='', password='password', email='email'
            )
        
