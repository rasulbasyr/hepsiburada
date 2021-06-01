# Generated by Django 3.1.4 on 2021-02-28 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0012_auto_20210228_1312'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(max_length=200, verbose_name='img')),
                ('alt_text', models.CharField(max_length=300, verbose_name='alt_text')),
            ],
            options={
                'verbose_name_plural': 'Afişler',
            },
        ),
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name_plural': 'Markalar'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Kategoriler'},
        ),
        migrations.AlterModelOptions(
            name='color',
            options={'verbose_name_plural': 'Renk Seçenekleri'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': 'İletişim '},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name_plural': 'Ürünler'},
        ),
        migrations.AlterModelOptions(
            name='productattribute',
            options={'verbose_name_plural': 'Ürün Özellikleri'},
        ),
        migrations.AlterModelOptions(
            name='size',
            options={'verbose_name_plural': 'Boyutlar'},
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email *'),
        ),
    ]