# Generated by Django 2.1.5 on 2021-08-19 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(default=1, upload_to='', verbose_name='Изображение'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Изображение'),
        ),
    ]
