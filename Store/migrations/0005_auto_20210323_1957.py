# Generated by Django 3.1.4 on 2021-03-23 16:57

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0004_auto_20210323_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddres',
            name='phone_number',
            field=phone_field.models.PhoneField(blank=True, help_text='Contact phone number', max_length=31),
        ),
    ]
