# Generated by Django 3.2.7 on 2021-11-26 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_cleaning'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cleaning',
            old_name='clean',
            new_name='technique',
        ),
    ]
