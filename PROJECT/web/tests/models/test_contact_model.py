import os
from django.core.exceptions import ValidationError

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PROJECT.settings")
import django

django.setup()
from unittest import TestCase
from PROJECT.web.models import ContactModel


class ContactModelTest(TestCase):
    def test_contact_model__whit_correct_model_validations__expect_success(self):
        '''
        first_name -> only letters
        last_name->only letters
        phone_number -> only digits
        :return: success
        '''
        contact = ContactModel(
            first_name='Hristina',
            last_name='Aleksandrova',
            email='a@abv.bg',
            phone_number='08888889',
            subject='default',
            content='This is a default content'
        )

        contact.save()

        self.assertIsNotNone(contact.pk)

    def test_contact_create__when_first_name_contains_a_digit__expect_to_fail(self):
        first_name = 'Hristina2'
        contact = ContactModel(
            first_name=first_name,
            last_name='Aleksandrova',
            email='a@abv.bg',
            phone_number='08888889',
            subject='default',
            content='This is a default content'
        )

        with self.assertRaises(ValidationError) as context:
            contact.full_clean()
            contact.save()
        self.assertIsNotNone(context.exception)

    def test_contact_create__when_first_name_contains_a_dollar_sign__expect_to_fail(self):
        first_name = 'Hristina$'
        contact = ContactModel(
            first_name=first_name,
            last_name='Aleksandrova',
            email='a@abv.bg',
            phone_number='08888889',
            subject='default',
            content='This is a default content'
        )

        with self.assertRaises(ValidationError) as context:
            contact.full_clean()
            contact.save()
        self.assertIsNotNone(context.exception)

    def test_contact_create__when_first_name_contains_a_space__expect_to_fail(self):
        first_name = 'Hristin  a'
        contact = ContactModel(
            first_name=first_name,
            last_name='Aleksandrova',
            email='a@abv.bg',
            phone_number='08888889',
            subject='default',
            content='This is a default content'
        )

        with self.assertRaises(ValidationError) as context:
            contact.full_clean()
            contact.save()
        self.assertIsNotNone(context.exception)

    def test_contact_create__when_last_name_contains_only_letters__expect_success(self):
        last_name = 'Aleksandrova'
        contact = ContactModel(
            first_name='Hristina',
            last_name=last_name,
            email='a@abv.bg',
            phone_number='08888889',
            subject='default',
            content='This is a default content'
        )

        with self.assertRaises(ValidationError) as context:
            contact.full_clean()
            contact.save()
        self.assertIsNotNone(context.exception)

    def test_contact_create__when_last_name_contains_a_digit__expect_to_fail(self):
        last_name = 'Aleksandrov55a'
        contact = ContactModel(
            first_name='Hristina',
            last_name=last_name,
            email='a@abv.bg',
            phone_number='08888889',
            subject='default',
            content='This is a default content'
        )

        with self.assertRaises(ValidationError) as context:
            contact.full_clean()
            contact.save()
        self.assertIsNotNone(context.exception)

    def test_contact_create__when_last_name_contains_a_dollar_sign__expect_to_fail(self):
        last_name = 'Aleksandrov$a'
        contact = ContactModel(
            first_name='Hristina',
            last_name=last_name,
            email='a@abv.bg',
            phone_number='08888889',
            subject='default',
            content='This is a default content'
        )

        with self.assertRaises(ValidationError) as context:
            contact.full_clean()
            contact.save()
        self.assertIsNotNone(context.exception)

    def test_contact_create__when_last_name_contains_a_space__expect_to_fail(self):
        last_name = 'Aleksandrov a'
        contact = ContactModel(
            first_name='Hristina',
            last_name=last_name,
            email='a@abv.bg',
            phone_number='08888889',
            subject='default',
            content='This is a default content'
        )

        with self.assertRaises(ValidationError) as context:
            contact.full_clean()
            contact.save()
        self.assertIsNotNone(context.exception)

    def test_contact_create__when_phone_number__contains_only_digit__expect_to_succeed(self):
        phone = '0088888889'
        contact = ContactModel(
            first_name='Hristina',
            last_name='Aleksandrova',
            email='a@abv.bg',
            phone_number=phone,
            subject='default',
            content='This is a default content'
        )

        with self.assertRaises(ValidationError) as context:
            contact.full_clean()
            contact.save()
        self.assertIsNotNone(context.exception)

    def test_contact_create__when_phone_number__contains_a_letter__expect_to_fail(self):
        phone = '0088888a89'
        contact = ContactModel(
            first_name='Hristina',
            last_name='Aleksandrova',
            email='a@abv.bg',
            phone_number=phone,
            subject='default',
            content='This is a default content'
        )

        with self.assertRaises(ValidationError) as context:
            contact.full_clean()
            contact.save()
        self.assertIsNotNone(context.exception)
    def test_contact_create__when_phone_number__contains_a_plus__expect_to_fail(self):
        phone = '+0088888a89'
        contact = ContactModel(
            first_name='Hristina',
            last_name='Aleksandrova',
            email='a@abv.bg',
            phone_number=phone,
            subject='default',
            content='This is a default content'
        )

        with self.assertRaises(ValidationError) as context:
            contact.full_clean()
            contact.save()
        self.assertIsNotNone(context.exception)
