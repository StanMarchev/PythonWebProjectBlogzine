from blogzine.utils.validators import validate_alphabet_characters_english
from django.contrib.auth.models import User, PermissionsMixin, UserManager
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.core.validators import MinLengthValidator
from django.db import models


class BlogzineUserManager(UserManager):
    pass


class BlogzineCenterUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        max_length=20,
        unique=True,
        validators=(
            validate_alphabet_characters_english,
            MinLengthValidator(5),
        )
    )

    email = models.EmailField(
        max_length=50,
        unique=True,
        validators=(
            validate_alphabet_characters_english,
            MinLengthValidator(5),
        )
    )

    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )

    is_verified = models.BooleanField(
        default=False,
    )

    is_active = models.BooleanField(
        default=True,
    )

    USERNAME_FIELD = 'username'

    objects = BlogzineUserManager()

    class Meta:
        verbose_name = 'blog_user'



class UserProfile(models.Model):
    user = models.OneToOneField(
        BlogzineCenterUser,
        on_delete=models.CASCADE
    )
    first_name = models.CharField(
        max_length=50
    )
    surname = models.CharField(
        max_length=50
    )
    profile_picture = models.ImageField(
        upload_to='profile_pics/',
        blank=True,
        null=True
    )
    location = models.CharField(
        max_length=100,
        blank=True
    )
    telephone_number = models.CharField(
        max_length=15,
        blank=True
    )
    interests = models.TextField(
        blank=True
    )

    def __str__(self):
        return f"{self.user.username}'s Profile"