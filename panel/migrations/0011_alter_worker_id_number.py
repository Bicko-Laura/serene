# Generated by Django 5.0.7 on 2024-11-30 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0010_worker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='Id_number',
            field=models.CharField(max_length=20),
        ),
    ]
