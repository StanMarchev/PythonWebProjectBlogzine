
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blogzine.common.urls')),
    path('auth/',include('blogzine.blog_auth.urls')),
    ]

