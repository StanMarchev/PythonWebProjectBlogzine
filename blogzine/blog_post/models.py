from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone

from blogzine.blog_auth.models import BlogzineCenterUser
from blogzine.utils.validators import validate_alphabet_characters_english


class CreatePost(models.Model):
    TOPIC_CHOICES = [
        ('post', 'Post'),
        ('question', 'Question'),
        ('poll', 'Poll'),
        ('images', 'Images'),
        ('video', 'Video'),
        ('other', 'Other'),
    ]

    CATEGORY_CHOICES = [
        ('lifestyle', 'Lifestyle'),
        ('technology', 'Technology'),
        ('travel', 'Travel'),
        ('business', 'Business'),
        ('sports', 'Sports'),
        ('marketing', 'Marketing'),
    ]

    post_name = models.CharField(
        max_length=50,
        validators=(
            validate_alphabet_characters_english,
            MinLengthValidator(5),
        )
    )
    post_type = models.CharField(max_length=20, choices=TOPIC_CHOICES)


    short_description = models.TextField(
        max_length=200,
        validators=(
            validate_alphabet_characters_english,
            MinLengthValidator(10),
        )
    )

    post_body = models.CharField(
        max_length=20,
        validators=(
            validate_alphabet_characters_english,
        )
    )
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    tags = models.CharField(max_length=20)

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, unique=False)

    author = models.ForeignKey(
        BlogzineCenterUser,
        on_delete=models.CASCADE,

    )

    created_on = models.DateTimeField(
        auto_now_add=True
    )

    id = models.AutoField(primary_key=True)


    class Meta:
        ordering = ['created_on']
        verbose_name = 'Discussion'

    def __str__(self):
        return self.post_name

