from django import forms

from profiles.models import Profile


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('nickname', 'first_name', 'last_name', 'chef')


class ProfileCreateForm(ProfileBaseForm):
    pass