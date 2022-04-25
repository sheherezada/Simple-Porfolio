from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from PROJECT.accounts.models import ProjectUser
from PROJECT.web.models import Quotes

UserModel = get_user_model()


class QuotesViewTest(TestCase):

    def test_get_expect_correct_template(self):
        response = self.client.get(reverse('quotes'))

        self.assertTemplateUsed(response, 'quotes.html')

