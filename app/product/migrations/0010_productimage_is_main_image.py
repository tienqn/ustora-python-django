# Generated by Django 3.2.22 on 2023-10-18 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_productimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='is_main_image',
            field=models.BooleanField(default=False),
        ),
    ]
