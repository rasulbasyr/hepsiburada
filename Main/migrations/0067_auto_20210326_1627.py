# Generated by Django 3.1.4 on 2021-03-26 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0066_auto_20210318_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='oldprice',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]