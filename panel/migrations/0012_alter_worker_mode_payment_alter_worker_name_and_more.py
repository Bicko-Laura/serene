# Generated by Django 5.0.7 on 2024-11-30 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0011_alter_worker_id_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='mode_payment',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='worker',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='worker',
            name='role',
            field=models.CharField(max_length=50),
        ),
    ]