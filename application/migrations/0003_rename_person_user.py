# Generated by Django 5.0.7 on 2024-12-04 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_remove_person_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='User',
        ),
    ]
