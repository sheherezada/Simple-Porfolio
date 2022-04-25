
from django.test import TestCase
from django.urls import reverse

from PROJECT.accounts.models import ProjectUser, Profile


class UserRegisterViewTest(TestCase):

    def test_get_expect_correct_template(self):
        response = self.client.get(reverse('register'))

        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_create_user_with_valid_data_expect_success(self):
        user_data = {
            'first_name': 'Penka',
            'last_name': 'Georgieva',
            'username': 'viktoriaaa',
            'password1': 'haakiri22',
            'password2': 'haakiri22',

            'phone': '0888885555',
            'email': 'v@abv.bg',

        }

        self.client.post(
            reverse('register'),
            data=user_data,
        )

        user_test = Profile.objects.first()
        self.assertIsNotNone(user_test)
        self.assertEqual(user_data['phone'], user_test.phone)
        self.assertEqual(user_data['first_name'], user_test.first_name)
        self.assertEqual(user_data['last_name'], user_test.last_name)
        self.assertEqual(user_data['email'], user_test.email)

    def test_create_user_with_invalid_data_expect_fail(self):
        user_data = {
            'first_name': 'Penka',
            'last_name': 'Georgieva',
            'username': 'viktoriaaa',
            'password1': 'haakiri22',
            'password2': 'haakiri99',

            'phone': '0888885555',
            'email': 'v@abv.bg',

        }

        self.client.post(
            reverse('register'),
            data=user_data,
        )

        user_test = Profile.objects.first()
        self.assertIsNotNone(user_test)
        self.assertEqual(user_data['phone'], user_test.phone)
        self.assertEqual(user_data['first_name'], user_test.first_name)
        self.assertEqual(user_data['last_name'], user_test.last_name)
        self.assertEqual(user_data['email'], user_test.email)

    def test_create_user_redirect(self):
        user_data = {
            'first_name': 'Penka',
            'last_name': 'Georgieva',
            'username': 'viktoriaaa',
            'password1': 'haakiri22',
            'password2': 'haakiri22',

            'phone': '0888885555',
            'email': 'v@abv.bg',

        }

        response = self.client.post(
            reverse('register'),
            data=user_data,
        )

        user_test = ProjectUser.objects.first()
        expect_url = reverse('dashboard')
        self.assertRedirects(response, expect_url)
