# Generated by Django 2.1.5 on 2021-08-18 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_auto_20210815_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(blank=True, choices=[('Лучшее', 'Лучшее'), ('Скидка', 'Скидка')], max_length=8, verbose_name='Статус'),
        ),
    ]
