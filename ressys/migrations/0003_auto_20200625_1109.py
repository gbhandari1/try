# Generated by Django 3.0.3 on 2020-06-25 16:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ressys', '0002_auto_20200622_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant',
            name='hired_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='applicant',
            name='create_date',
            field=models.DateField(default=datetime.date(2020, 6, 25)),
        ),
    ]
