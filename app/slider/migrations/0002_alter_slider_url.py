# Generated by Django 3.2.22 on 2023-10-13 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='url',
            field=models.ImageField(upload_to='images/sliders'),
        ),
    ]