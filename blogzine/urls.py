
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogzine.common.urls')),
    path('accounts/', include('blogzine.blog_auth.urls')),
    path('posts/', include('blogzine.blog_post.urls')),
    path('shop/', include('blogzine.blog_shop.urls')),

    ]

