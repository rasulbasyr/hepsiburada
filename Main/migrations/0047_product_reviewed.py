# Generated by Django 3.1.4 on 2021-03-10 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0046_remove_product_indirsim'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='reviewed',
            field=models.BooleanField(default=False),
        ),
    ]