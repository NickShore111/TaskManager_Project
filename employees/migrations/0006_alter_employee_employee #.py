# Generated by Django 3.2.7 on 2021-10-10 02:24

from django.db import migrations, models
import employees.validators


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0005_alter_employee_employee #'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Employee #',
            field=models.CharField(help_text='4 digit pin', max_length=4, unique=True, validators=[employees.validators.validate_employee_number]),
        ),
    ]
