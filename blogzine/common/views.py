from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):
    template_name = 'common/index.html'

class AboutView(TemplateView):
    template_name = 'common/about-us.html'
class DashboardView(LoginRequiredMixin , TemplateView):
     template_name = 'common/dashboard.html'
