from django.contrib.auth.models import User
from django.views import generic as views

from blogzine.blog_auth.forms.user_profile import ProfileEdit
from blogzine.blog_auth.models import BlogzineCenterUser


class ProfileDetailsView(views.DetailView):
    pass



class ProfileEditView(views.UpdateView):

    template_name = 'auth/dashboard-edit-profile.html'




class ProfileDeleteView(views.DeleteView):
    pass