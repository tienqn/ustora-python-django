# Generated by Django 3.2.22 on 2023-10-13 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0005_alter_slider_sub_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='sub_title',
            field=models.CharField(default='', max_length=255),
        ),
    ]
