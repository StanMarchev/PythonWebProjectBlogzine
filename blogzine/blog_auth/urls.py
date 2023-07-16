from django.contrib.auth import login
from django.urls import path

from blogzine.blog_auth.views.auth import SignUpView, SignInView, SignOutView, RequireSignInView

urlpatterns=[
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
    path('sign-in-required/', RequireSignInView.as_view(), name='require sign in'),
]