# Generated by Django 3.2.22 on 2023-10-13 03:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_viewedproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewedproduct',
            name='view_time',
            field=models.DateTimeField(),
        ),
    ]
