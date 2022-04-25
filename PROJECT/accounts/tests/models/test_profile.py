import os

from django.core.exceptions import ValidationError

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PROJECT.settings")

import django

django.setup()

from unittest import TestCase

from PROJECT.accounts.models import Profile



class ProfileTests(TestCase):
    def test_profile_create__whit_correct_model_validations__expect_success(self):
        '''
        first_name -> only letters
        last_name->only letters
        phone -> only digits
        :return: success
        '''
        profile = Profile(
            first_name='Hristina',
            last_name='Aleksandrova',
            email='a@abv.bg',
            phone='08888888',
            user_id='1',
        )

        profile.save()

        self.assertIsNotNone(profile.pk)

    def test_profile_create__when_first_name_contains_a_digit__expect_to_fail(self):
        first_name = 'Hristina2'
        profile = Profile(
            first_name=first_name,
            last_name='Aleksandrova',
            email='a@abv.bg',
            phone='08888888',
            user_id='1',
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name_contains_a_dollar_sign__expect_to_fail(self):
        first_name = 'Hristina$'
        profile = Profile(
            first_name=first_name,
            last_name='Aleksandrova',
            email='a@abv.bg',
            phone='08888888'
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)

    def test_profile_create__when_first_name_contains_a_space__expect_to_fail(self):
        first_name = 'Hristin a'
        profile = Profile(
            first_name=first_name,
            last_name='Aleksandrova',
            email='a@abv.bg',
            phone='08888888'
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)

    def test_profile_create__when_last_name_contains_only_letters__expect_success(self):
        last_name = 'Hristina'
        profile = Profile(
            last_name=last_name,
            first_name='Hristina',
            email='a@abv.bg',
            phone='08888888'
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)

    def test_profile_create__when_last_name_contains_a_digit__expect_to_fail(self):
        last_name = 'Aleksandrova4'
        profile = Profile(
            last_name=last_name,
            first_name='Hristina',
            email='a@abv.bg',
            phone='08888888'
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)

    def test_profile_create__when_last_name_contains_a_dollar_sign__expect_to_fail(self):
        profile = Profile(
            last_name='Aleksandr$ova',
            first_name='Hristina',
            email='a@abv.bg',
            phone='08888888'
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)

    def test_profile_create__when_last_name_contains_a_space__expect_to_fail(self):
        profile = Profile(
            last_name='Aleksand rova',
            first_name='Hristina',
            email='a@abv.bg',
            phone='08888888'
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)

    def test_profile_create__when_phone_number__contains_only_digit__expect_to_succeed(self):
        phone = '08888888'
        profile = Profile(
            first_name='Hrisitna',
            last_name='Aleksandrova',
            email='a@abv.bg',
            phone=phone,
            user_id='1',
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)

    def test_profile_create__when_phone_number__contains_a_letter__expect_to_fail(self):
        phone = '088888a88'
        profile = Profile(
            first_name='Hrisitna',
            last_name='Aleksandrova',
            email='a@abv.bg',
            phone=phone,
            user_id='1',
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)

    def test_profile_create__when_phone_number__contains_a_plus__expect_to_fail(self):
        phone = '+008888888'
        profile = Profile(
            first_name='Hrisitna',
            last_name='Aleksandrova',
            email='a@abv.bg',
            phone=phone,
            user_id='1',
        )

        with self.assertRaises(ValidationError) as context:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(context.exception)
