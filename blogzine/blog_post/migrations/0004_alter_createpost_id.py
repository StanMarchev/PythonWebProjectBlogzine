# Generated by Django 4.2.3 on 2023-08-05 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0003_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpost',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
