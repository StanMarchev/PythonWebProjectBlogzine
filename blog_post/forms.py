from django import forms
from .models import CreatePost

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = CreatePost
        fields = '__all__'
