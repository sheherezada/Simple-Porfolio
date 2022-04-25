from PROJECT.accounts.models import Profile
from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model
from PROJECT.common.helpers import BootstrapFormMixin


class CreateProfileForm(BootstrapFormMixin, auth_forms.UserCreationForm):
    first_name = forms.CharField(
        max_length=Profile.FIRST_NAME_MAX_LEN,
    )
    last_name = forms.CharField(
        max_length=Profile.LAST_NAME_MAX_LEN,
    )

    email = forms.TextInput(

    ),

    phone = forms.TextInput()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_bootstrap_form_controls()

    def save(self, commit=True):
        user = super().save(commit=commit)

        profile = Profile(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            phone = self.cleaned_data['phone'],

            email=self.cleaned_data['email'],

            user=user,
        )

        if commit:
            profile.save()
        return user

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'phone', 'email', 'username', 'password1' )



