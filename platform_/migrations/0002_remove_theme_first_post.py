# Generated by Django 4.2.5 on 2024-02-22 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('platform_', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='first_post',
        ),
    ]
