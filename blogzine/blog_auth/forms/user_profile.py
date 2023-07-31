from django import forms

from blogzine.blog_auth.models import  UserProfile


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'surname', 'profile_picture', 'location', 'telephone_number', 'interests']