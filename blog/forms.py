from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Submit
from django import forms
from django.forms import TextInput

from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    text_color = forms.CharField(widget=TextInput(attrs={'type': 'color'}))
    background_color = forms.CharField(widget=TextInput(attrs={'type': 'color'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('content'),
            Field('colored', x_model='colored'),
            Fieldset(
                'Colors',
                'text_color',
                'background_color',
                x_show='colored'
            ),
            Submit('submit', 'Submit')
        )

    class Meta:
        model = Post
        fields = ['content', 'colored', 'text_color', 'background_color']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']


class SearchForm(forms.Form):
    q = forms.CharField(required=False, label="Search")
