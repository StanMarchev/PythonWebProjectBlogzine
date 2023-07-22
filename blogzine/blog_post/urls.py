from django.urls import path, include

from blogzine.blog_post.views import PostDetailsView, PostCreateView, PostEditView

urlpatterns = [
    path('posts/<int:pk>/', include([
        path('', PostDetailsView.as_view(), name='post-details'),
        path('create/', PostCreateView.as_view(), name='post-create'),
        path('edit/', PostEditView.as_view(), name='post-edit'),
 ]))
]