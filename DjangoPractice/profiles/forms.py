from django import forms

from DjangoPractice.mixins import PlaceholderMixin
from profiles.models import Profile


class ProfileBaseForm(PlaceholderMixin, forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"



class ProfileCreateForm(ProfileBaseForm):
    widgets = {
        'email': forms.TextInput(attrs={'placeholder': 'Enter your username'}),

    }


class ProfileDeleteForm(ProfileBaseForm):
    pass