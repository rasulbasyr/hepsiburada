# Generated by Django 3.1.4 on 2021-03-24 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0010_remove_shippingaddres_address_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddres',
            name='city',
            field=models.CharField(max_length=200, verbose_name='İl'),
        ),
    ]