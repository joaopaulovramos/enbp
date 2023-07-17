# Generated by Django 3.1.7 on 2023-07-14 20:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('level', models.PositiveIntegerField(choices=[(10, 'Debug'), (20, 'Info'), (30, 'Warning'), (40, 'Error'), (50, 'Critical')], default=20)),
                ('action_time', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='action time')),
            ],
            options={
                'verbose_name': 'log entry',
                'verbose_name_plural': 'log entries',
                'ordering': ('-action_time',),
            },
        ),
    ]