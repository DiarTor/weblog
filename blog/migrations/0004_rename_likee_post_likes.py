# Generated by Django 4.2 on 2023-04-12 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_likee_like'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='likee',
            new_name='likes',
        ),
    ]
