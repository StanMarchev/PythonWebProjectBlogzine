from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView, TemplateView




#from blogzine.blog_auth.models import BlogUser

#FIX ME !!!
class SignUpView(CreateView):
    template_name = 'auth/signup.html'


class SignInView(LoginView):
    template_name = 'signin.html'


class SignOutView(LogoutView):
    template_name = 'common/index.html'

class RequireSignInView(TemplateView):
    pass