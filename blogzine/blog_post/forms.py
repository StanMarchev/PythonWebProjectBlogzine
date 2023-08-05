from django import forms
from .models import CreatePost

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = CreatePost
        fields = ['post_name', 'post_type', 'short_description', 'post_body', 'file', 'tags', 'category']
