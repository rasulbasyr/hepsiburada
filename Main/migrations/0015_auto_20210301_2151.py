# Generated by Django 3.1.4 on 2021-03-01 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0014_product_is_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
        migrations.AlterField(
            model_name='product',
            name='is_featured',
            field=models.BooleanField(default=False, verbose_name='is_featured'),
        ),
    ]
