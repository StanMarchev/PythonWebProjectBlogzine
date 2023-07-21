
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect

from blogzine.blog_auth.forms.auth import SignUpForm, SignInForm
from blogzine.blog_auth.models import BlogzineCenterUser


class SignUpView(CreateView):
    template_name = 'auth/signup.html'
    model = BlogzineCenterUser
    form_class = SignUpForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response=super().form_valid(form)
        login(self.request, self.object)
        return response



class SignInView(LoginView):
    template_name = 'auth/signin.html'
    form_class = SignInForm
    redirect_authenticated_user = True


class SignOutView(LogoutView):
    template_name = 'common/index.html'
    next_page = 'home'


class RequireSignInView(TemplateView):
     template_name = 'common/dashboard.html'