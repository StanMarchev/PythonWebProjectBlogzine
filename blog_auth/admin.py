





from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from blogzine.blog_auth.models import BlogzineCenterUser


@admin.register(BlogzineCenterUser)
class BlogzineCenterUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'is_staff')
    list_filter = ('is_staff',)
    ordering = ('email',)
    fieldsets = (
        (None, {'fields': ('email',
                           'password',
                           'is_staff',
                           'is_superuser',
                           'is_verified',
                           'is_active',
                           'date_joined',
                           )}),
        ('Permissions', {
            'fields': ('groups', 'user_permissions'),
        }),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    readonly_fields = ('date_joined',)