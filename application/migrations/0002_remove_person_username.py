# Generated by Django 5.0.7 on 2024-12-04 04:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='username',
        ),
    ]