# Generated by Django 3.1.4 on 2021-02-25 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0005_productattribute'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
    ]
