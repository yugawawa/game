# Generated by Django 4.0.3 on 2022-03-27 11:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todoApp', '0004_alter_todoinf_deadline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoinf',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2022, 3, 27, 11, 45, 48, 152020, tzinfo=utc)),
        ),
    ]