# Generated by Django 2.0.2 on 2018-05-16 21:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180516_2124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 16, 21, 24, 39, 619920, tzinfo=utc)),
        ),
    ]
