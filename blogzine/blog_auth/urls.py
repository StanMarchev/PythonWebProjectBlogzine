
from django.urls import path , include

from blogzine.blog_auth.views.auth import SignUpView, SignInView, SignOutView, RequireSignInView
from blogzine.blog_auth.views.user_profile import view_profile, edit_profile

urlpatterns=[
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
    path('sign-in-required/', RequireSignInView.as_view(), name='require sign in'),
    path('edit/', edit_profile, name='profile-edit'),
    path('profile/<int:pk>/', include([
        path('', view_profile, name='profile-details'),

        #path('delete/', ProfileDeleteView.as_view(), name='profile-delete')
    ]))
]