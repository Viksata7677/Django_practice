from django import forms

from profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')  # Base fields
        widgets = {
            'password': forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
        }


class ProfileCreateForm(ProfileBaseForm):
    pass


class ProfileEditForm(ProfileBaseForm):
    class Meta(ProfileBaseForm.Meta):  # Inherit Meta from ProfileBaseForm
        fields = '__all__'

