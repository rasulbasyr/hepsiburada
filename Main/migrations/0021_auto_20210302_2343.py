# Generated by Django 3.1.4 on 2021-03-02 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0020_auto_20210302_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='category_imgs/'),
        ),
    ]
