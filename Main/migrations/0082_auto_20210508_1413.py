# Generated by Django 3.1.4 on 2021-05-08 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0081_comments_star'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='star',
            field=models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Star'),
        ),
    ]
