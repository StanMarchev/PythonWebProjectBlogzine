# Generated by Django 4.2.3 on 2023-08-05 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0005_alter_createpost_post_body_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpost',
            name='category',
            field=models.CharField(choices=[('lifestyle', 'Lifestyle'), ('technology', 'Technology'), ('travel', 'Travel'), ('business', 'Business'), ('sports', 'Sports'), ('marketing', 'Marketing')], max_length=50),
        ),
    ]
