# Generated by Django 3.1.4 on 2021-03-12 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0056_auto_20210313_0127'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LastReview',
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Ürünler'},
        ),
    ]
