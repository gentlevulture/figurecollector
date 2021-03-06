# Generated by Django 3.2.7 on 2021-11-24 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cleaning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Cleaning Date')),
                ('clean', models.CharField(choices=[('D', 'Dry'), ('A', 'Alcohol'), ('Q', 'Q-Tip')], default='D', max_length=1)),
                ('figure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.figure')),
            ],
        ),
    ]
