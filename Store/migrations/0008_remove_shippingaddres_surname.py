# Generated by Django 3.1.4 on 2021-03-24 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0007_auto_20210325_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddres',
            name='surname',
        ),
    ]
