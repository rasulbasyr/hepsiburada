# Generated by Django 3.1.4 on 2021-03-17 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0063_auto_20210317_1941'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='reviewed',
        ),
    ]
