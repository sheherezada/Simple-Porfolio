from django.test import TestCase
from django.urls import reverse

from PROJECT.web.models import Portfolio


class PortfolioViewTests(TestCase):
    def test_get_expect_correct_template(self):
        response = self.client.get(reverse('portfolio item'))

        self.assertTemplateUsed(response, 'portfolio-item.html')

    def test_correct_context_portfolio_view(self):
        portfolio_items_to_create = (
            Portfolio(
                description='default',
                type='default',
                name='portfolio item',
                image='mediafiles/img1_Kyde0af.jpg',
            ),
            Portfolio(
                description='default2',
                type='default2',
                name='portfolio item2',
                image='mediafiles/img1_Kyde0af.jpg',
            )

        )

        Portfolio.objects.bulk_create(portfolio_items_to_create)

        response = self.client.get(reverse('portfolio item'))

        portfolio_items = response.context
        self.assertEqual(len(portfolio_items), 2)
