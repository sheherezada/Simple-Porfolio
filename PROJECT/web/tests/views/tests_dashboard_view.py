from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


from PROJECT.web.views import DashboardView

UserModel = get_user_model()


class DashboardListViewTest(TestCase):
    def test_get_expect_correct_template(self):
        response = self.client.get(reverse('dashboard'))

        self.assertTemplateUsed(response, 'dashboard.html')

    def test_dashboard_template_context_correct_user_name_shown(self):


        user_data = {
            'username': 'viktoria',
            'password': 'haakiri22',
            'phone': '0888885555',
            'email': 'v@abv.bg',

        }
        """
        assert str(dict[key]) in str(query_set)
        """
        assert_data = next(iter(user_data.items()))
        user_data_username = str(user_data['username'])

        UserModel.objects.create_user(**user_data)
        self.client.login(**user_data)

        response = self.client.get(reverse('dashboard'))

        query_set_str = str(response.context[DashboardView.context_object_name])
        self.assertIn(
            user_data_username,
            query_set_str
        )

    def test_dashboard_template_context_wrong_user_name_shown_expected_failure(self):


        user_data = {
            'username': 'viktoria',
            'password': 'haakiri22',
            'phone': '0888885555',
            'email': 'v@abv.bg',

        }
        """
        assert str(dict[key]) in str(query_set)
        """
        assert_data = next(iter(user_data.items()))
        user_data_username = 'default'

        UserModel.objects.create_user(**user_data)
        self.client.login(**user_data)

        response = self.client.get(reverse('dashboard'))

        query_set_str = str(response.context[DashboardView.context_object_name])
        self.assertIn(
            user_data_username,
            query_set_str
        )
