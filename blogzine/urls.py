from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogzine.common.urls')),
    path('accounts/', include('blogzine.blog_auth.urls')),
    path('posts/', include('blogzine.blog_post.urls')),
    path('shop/', include('blogzine.blog_shop.urls')),
    path('posts/', include('blogzine.comments.urls')),

    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)