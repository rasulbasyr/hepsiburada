# Generated by Django 3.1.4 on 2021-05-08 10:52

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0079_auto_20210507_2258'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='user',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='comments',
            name='dislikes',
            field=models.ManyToManyField(blank=True, related_name='Related_comment_dislike', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comments',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='Related_comment_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
