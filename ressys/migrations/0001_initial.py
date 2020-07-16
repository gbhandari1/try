# Generated by Django 3.0.3 on 2020-06-22 15:17

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=256)),
                ('lname', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('hired', models.BooleanField(default=False)),
                ('goal_oriented', models.TextField()),
                ('improvement_oriented', models.TextField()),
                ('success_record', models.TextField()),
                ('culture_fit', models.TextField()),
                ('communication', models.TextField()),
                ('ratings', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
            ],
        ),
    ]