from django.urls import path
from . import views
from .views import CommentView

urlpatterns = [
    path('<int:post_id>/', CommentView.as_view(), name='post-comments'),
]
