# Generated by Django 3.1.4 on 2021-03-06 17:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main', '0033_auto_20210306_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='size2',
        ),
        migrations.AddField(
            model_name='product',
            name='a',
            field=models.ManyToManyField(default=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
