# Generated by Django 3.1.4 on 2021-03-18 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0065_auto_20210317_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]