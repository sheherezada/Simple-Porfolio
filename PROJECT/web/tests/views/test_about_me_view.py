from django.test import TestCase
from django.urls import reverse

from PROJECT.web.models import  Projects


class AboutMeViewTests(TestCase):
    def test_get_expect_correct_template(self):
        response = self.client.get(reverse('about me'))

        self.assertTemplateUsed(response, 'about-me.html')

    def test_correct_context_about_me_view(self):
        projects_to_create = (
            Projects(
                name='default',
                description='default',

                ),
            Projects(
                name='default2',
                description='default2',
                ),

            )

        Projects.objects.bulk_create(projects_to_create)

        response = self.client.get(reverse('portfolio item'))

        project_items = response.context
        self.assertEqual(len(project_items), 2)
