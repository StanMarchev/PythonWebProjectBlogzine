from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic as views

from blogzine.blog_auth.forms.user_profile import ProfileEdit
from blogzine.blog_auth.models import BlogzineCenterUser


class ProfileDetailsView(views.DetailView):
    pass



class ProfileEditView(views.UpdateView):
    model = BlogzineCenterUser
    template_name = 'auth/dashboard-edit-profile.html'
    success_url = reverse_lazy('dashboard')
    fields = '__all__'




class ProfileDeleteView(views.DeleteView):
    pass