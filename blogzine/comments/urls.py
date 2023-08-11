from django.urls import path
from . import views
from .views import CommentView


urlpatterns = [
    path('<int:pk>/comments/', CommentView.as_view(), name='post-comments'),
]
