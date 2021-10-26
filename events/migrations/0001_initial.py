# Generated by Django 3.2.7 on 2021-10-25 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=45, null=True)),
                ('notes', models.TextField(blank=True, max_length=200, null=True, verbose_name='Event Notes')),
                ('day', models.DateField(blank=True, help_text='Day of the event', null=True)),
                ('start_time', models.TimeField(blank=True, help_text='Starting time', null=True)),
                ('end_time', models.TimeField(blank=True, help_text='Final time', null=True)),
                ('created_by', models.CharField(blank=True, max_length=45, null=True)),
                ('created_for', models.CharField(blank=True, max_length=45, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'events',
            },
        ),
        migrations.CreateModel(
            name='EventsHasEmployees',
            fields=[
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='events.events')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employees.employees')),
            ],
            options={
                'db_table': 'events_has_employees',
                'unique_together': {('event', 'employee')},
            },
        ),
    ]
