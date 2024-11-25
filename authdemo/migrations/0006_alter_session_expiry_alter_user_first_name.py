# Generated by Django 5.1.1 on 2024-11-06 09:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authdemo', '0005_alter_session_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='expiry',
            field=models.DurationField(default=datetime.timedelta(seconds=1200)),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
