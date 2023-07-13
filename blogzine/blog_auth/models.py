# from blogzine.utils.validators import validate_alphabet_characters_english
# from django.contrib.auth.models import User, PermissionsMixin, UserManager
# from django.contrib.auth.base_user import AbstractBaseUser
# from django.core.validators import MinLengthValidator
# from django.db import models
#
#
# class BlogUserManager(UserManager):
#     pass
#
#
# class BlogUser(AbstractBaseUser, PermissionsMixin):
#     username = models.CharField(
#         max_length=20,
#         unique=True,
#         validators=(
#             validate_alphabet_characters_english,
#             MinLengthValidator(5),
#         )
#     )
#
#     email = models.EmailField(
#         max_length=50,
#         unique=True,
#         validators=(
#             validate_alphabet_characters_english,
#             MinLengthValidator(5),
#         )
#     )
#
#     is_staff = models.BooleanField(
#         default=False,
#     )
#     date_joined = models.DateTimeField(
#         auto_now_add=True,
#     )
#
#     is_verified = models.BooleanField(
#         default=False,
#     )
#
#     is_active = models.BooleanField(
#         default=True,
#     )
#
#     USERNAME_FIELD = 'username'
#
#     objects = BlogUserManager()
#
#     class Meta:
#         verbose_name = 'User'