# Generated by Django 3.1.4 on 2021-05-22 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0025_auto_20210517_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shippingaddres',
            name='order',
        ),
        migrations.AddField(
            model_name='shippingaddres',
            name='order',
            field=models.ManyToManyField(blank=True, to='Store.Order'),
        ),
    ]
