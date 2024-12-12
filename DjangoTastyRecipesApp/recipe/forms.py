from django import forms

from recipe.models import Recipe


class RecipeBaseForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('title', 'cuisine_type', 'ingredients', 'instructions', 'cooking_time', 'image_url')
        widgets = {
            'ingredients': forms.Textarea(attrs={'placeholder': "ingredient1, ingredient2, ..."}),
            'instructions': forms.Textarea(attrs={'placeholder': "Enter detailed instructions here..."}),
            'cooking_time': forms.NumberInput(attrs={'placeholder': 'Enter cooking time in minutes'}),
            'image_url': forms.URLInput(attrs={'placeholder': "Optional image URL here..."}),
        }


class RecipeCreateForm(RecipeBaseForm):
    pass


class RecipeEditForm(RecipeBaseForm):
    pass