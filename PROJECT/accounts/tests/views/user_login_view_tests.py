from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from PROJECT.accounts.models import ProjectUser

UserModel = get_user_model()


class UserLoginViewTest(TestCase):

    def test_get_expect_correct_template(self):
        response = self.client.get(reverse('login user'))

        self.assertTemplateUsed(response, 'accounts/login.html')

    def test_user_login_redirect(self):
        user_data = {
            'username': 'viktoria',
            'password': 'harakiri22',
            'phone': '0888885555',
            'email': 'v@abv.bg',
        }


        UserModel.objects.create_user(**user_data)
        self.client.login(**user_data)

        response = self.client.post(
            reverse('show index'),
            data={
                'username': user_data['username'],
                'password': user_data['password'],

            }

        )

        user_test = ProjectUser.objects.first()

        self.assertIsNotNone(user_test)
        expect_url = reverse('dashboard')
        self.assertRedirects(response, expect_url)
