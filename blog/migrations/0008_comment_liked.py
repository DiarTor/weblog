# Generated by Django 4.2 on 2023-04-20 04:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0007_delete_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='liked',
            field=models.ManyToManyField(blank=True, default=None, related_name='like_comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
