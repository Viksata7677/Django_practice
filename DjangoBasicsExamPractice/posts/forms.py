from django import forms

from posts.models import Post


class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('author',)


class PostCreateForm(PostBaseForm):
    widgets = {
        'title': forms.TextInput(attrs={'placeholder': 'Put an attractive and unique title...'}),
        'image_url': forms.TextInput(attrs={'placeholder': 'Share your funniest furry photo URL!'}),
        'content': forms.Textarea(attrs={'placeholder': 'Share some interesting facts about your adorable pets...'}),

    }

    labels = {
        'image_url': 'Post Image URL:',
        'content': 'Content:',
    }


class PostEditForm(PostBaseForm):
    pass


class PostDeleteForm(PostBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.disabled = True


#TODO: CREATE POST PLACEHOLDERS MISSING!