# Generated by Django 3.1.4 on 2021-03-02 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0017_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='category_imgs/'),
        ),
    ]
