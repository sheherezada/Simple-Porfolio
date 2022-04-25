from django import forms


from PROJECT.common.helpers import BootstrapFormMixin
from PROJECT.web.models import Quotes, ContactModel




class CreateQuoteForm(BootstrapFormMixin, forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user
        self._init_bootstrap_form_controls()

    def save(self, commit=True):

        quotes = super().save(commit=False)

        quotes.user = self.user
        if commit:
            quotes.save()

        return quotes

    class Meta:
        model = Quotes
        fields = ('type', 'description')
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'placeholder': 'Enter type of service',
                }
            ),
            'description': forms.Textarea(
                attrs={
                    'placeholder': 'Enter details',

                }
            ),
        }


class ContactFormForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your first name',
                },
            ),
            'last_name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your last name',
                },
            ),

            'phone_number' : forms.TextInput(
                attrs={
                    'placeholder': 'Enter your phone number',
                },
            ),

            'email': forms.TextInput(
                attrs={
                    'placeholder': 'Enter your email',
                }
            ),
            'subject': forms.TextInput(
                attrs={
                    'placeholder': 'Enter subject',
                },
            ),

            'content': forms.Textarea(
                attrs={
                    'placeholder': 'Enter details of your request',

                }
            ),

        }

#

