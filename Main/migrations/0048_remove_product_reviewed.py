# Generated by Django 3.1.4 on 2021-03-10 05:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0047_product_reviewed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='reviewed',
        ),
    ]