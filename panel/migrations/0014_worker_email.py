# Generated by Django 5.0.7 on 2024-11-30 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0013_worker_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='email',
            field=models.EmailField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
