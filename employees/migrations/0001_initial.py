# Generated by Django 3.2.7 on 2021-10-26 22:00

from django.db import migrations, models
import django.db.models.deletion
import employees.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, choices=[('FoH', 'Foh'), ('BoH', 'Boh')], max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'db_table': 'departments',
            },
        ),
        migrations.CreateModel(
            name='Positions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, choices=[('1', 'Manager'), ('2', 'Assistant Manager'), ('3', 'Supervisor'), ('4', 'Server'), ('5', 'Busser'), ('6', 'Bartender'), ('7', 'Expo'), ('8', 'Host'), ('9', 'Barback'), ('20', 'Chef'), ('21', 'Sous Chef'), ('22', 'Pantry'), ('23', 'Line Cook'), ('24', 'Grill Cook'), ('25', 'Prep Cook'), ('26', 'Fry Cook'), ('27', 'Dishwasher')], max_length=45, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='employees.departments')),
            ],
            options={
                'db_table': 'positions',
            },
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_num', models.CharField(help_text='4 digit pin', max_length=4, validators=[employees.validators.validate_employee_number], verbose_name='Employee #')),
                ('username', models.CharField(max_length=45)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=45)),
                ('phone', models.CharField(max_length=45)),
                ('start_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='employees.positions')),
            ],
            options={
                'db_table': 'employees',
            },
        ),
    ]
