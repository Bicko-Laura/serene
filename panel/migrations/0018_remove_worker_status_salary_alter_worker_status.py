# Generated by Django 5.0.7 on 2024-12-01 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0017_worker_status_salary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='worker',
            name='status_salary',
        ),
        migrations.AlterField(
            model_name='worker',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
    ]
