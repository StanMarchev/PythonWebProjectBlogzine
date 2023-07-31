
from django.urls import path

from blogzine.blog_auth import views
from blogzine.blog_auth.views.auth import SignUpView, SignInView, SignOutView, RequireSignInView
from blogzine.blog_auth.views.user_profile import edit_profile, view_profile

urlpatterns=[
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
    path('sign-in-required/', RequireSignInView.as_view(), name='require sign in'),
    path('edit/', edit_profile, name='profile-edit'),
    path('profile/', view_profile, name='profile'),

        #path('delete/', ProfileDeleteView.as_view(), name='profile-delete')

]