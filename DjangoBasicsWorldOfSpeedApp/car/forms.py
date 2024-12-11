from django import forms
from car.models import Car


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        exclude = ('owner',)
        widgets = {
            'image_url': forms.URLInput(attrs={'placeholder': 'https://...'}),
        }
        error_messages = {
            'image_url': {
                'unique': "This image URL is already in use! Provide a new one.",
            },
        }


class CarCreateForm(CarBaseForm):
    pass


class CarEditForm(CarBaseForm):
    pass


class CarDeleteForm(CarBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = True
