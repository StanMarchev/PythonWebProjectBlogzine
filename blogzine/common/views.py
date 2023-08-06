from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView

from blogzine.blog_auth.forms.user_profile import ProfileEditForm
from blogzine.blog_post.models import Post, CreatePost


class HomeView(TemplateView):
    template_name = 'common/index.html'

class AboutView(TemplateView):
    template_name = 'common/about-us.html'
class DashboardView(LoginRequiredMixin , TemplateView):
    template_name = 'common/dashboard.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = CreatePost.objects.all()
        return context
