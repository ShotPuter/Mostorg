# Generated by Django 2.1.5 on 2021-08-15 16:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20210815_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='Описание'),
        ),
    ]
