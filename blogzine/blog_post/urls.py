from django.urls import path, include

from blogzine.blog_post.views import PostDetailsView, PostCreateView, PostEditView, PostListView

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<int:pk>/', include([
        path('', PostDetailsView.as_view(), name='post-details'),
        path('post-list', PostListView.as_view(), name='post-list'),
        path('edit/', PostEditView.as_view(), name='post-edit'),
 ]))
]