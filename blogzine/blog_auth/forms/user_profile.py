from django import forms

from blogzine.blog_auth.models import BlogzineCenterUser


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = BlogzineCenterUser
        fields = ['username', 'email']