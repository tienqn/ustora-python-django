# Generated by Django 3.2.22 on 2023-10-19 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_producttag_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='', max_length=255),
        ),
    ]
