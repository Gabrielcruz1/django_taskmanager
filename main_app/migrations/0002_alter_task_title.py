# Generated by Django 4.1.5 on 2023-01-30 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.TextField(max_length=500),
        ),
    ]
