# Generated by Django 3.1.4 on 2021-03-12 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0054_auto_20210310_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('review', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Ürünü son goruntuleme',
                'ordering': ['-time'],
            },
        ),
    ]