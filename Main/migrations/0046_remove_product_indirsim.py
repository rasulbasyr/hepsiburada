# Generated by Django 3.1.4 on 2021-03-07 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0045_auto_20210307_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='indirsim',
        ),
    ]
