from django import forms

from author.models import Author


class AuthorBaseForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': "Enter your first name..."}),
            'last_name': forms.TextInput(attrs={'placeholder': "Enter your last name..."}),
            'passcode': forms.PasswordInput(attrs={'placeholder': "Enter 6 digits"}),
            'pets_number': forms.TextInput(attrs={'placeholder': "Enter the number of your pets..."}),
        }
        labels = {
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'passcode': 'Passcode:',
            'pets_number': 'Pets Number:',
        }


class AuthorCreateForm(AuthorBaseForm):
    pass


class AuthorEditForm(AuthorBaseForm):
    pass


class AuthorDeleteForm(AuthorBaseForm):
    pass