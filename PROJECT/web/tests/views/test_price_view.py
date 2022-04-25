from django.test import TestCase
from django.urls import reverse




class PriceViewTests(TestCase):
    def test_get_expect_correct_template(self):
        response = self.client.get(reverse('price'))

        self.assertTemplateUsed(response, 'price.html')