# Generated by Django 5.1.6 on 2025-03-18 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dept_id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('dept_name', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=300)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('WeekOff', models.IntegerField(choices=[(0, 'Monday'), (1, 'Tuesday'), (2, 'Wednesday'), (3, 'Thursday'), (4, 'Friday'), (5, 'Saturday')], default=5)),
            ],
        ),
    ]
