# Generated by Django 2.1.5 on 2021-08-19 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20210819_2214'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testominal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя Фамилия')),
                ('work', models.CharField(blank=True, max_length=200, verbose_name='Должность')),
                ('image', models.ImageField(upload_to='', verbose_name='Фото')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
