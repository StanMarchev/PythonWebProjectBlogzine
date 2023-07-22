from django.contrib.auth import login
from django.urls import path , include

from blogzine.blog_auth.views.auth import SignUpView, SignInView, SignOutView, RequireSignInView
from blogzine.blog_auth.views.user_profile import ProfileDetailsView, ProfileEditView, ProfileDeleteView

urlpatterns=[
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('sign-in/', SignInView.as_view(), name='sign-in'),
    path('sign-out/', SignOutView.as_view(), name='sign-out'),
    path('sign-in-required/', RequireSignInView.as_view(), name='require sign in'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='profile-details'),
        path('edit/', ProfileEditView.as_view(), name='profile-edit'),
        path('delete/', ProfileDeleteView.as_view(), name='profile-delete')
    ]))
]