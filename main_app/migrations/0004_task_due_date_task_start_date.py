# Generated by Django 4.1.6 on 2023-02-03 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_task_options_task_complete_task_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='start_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
