# Generated by Django 3.2.7 on 2021-10-10 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_alter_employee_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='employee',
            field=models.ForeignKey(default='99', on_delete=django.db.models.deletion.DO_NOTHING, to='employees.employee'),
        ),
        migrations.AddField(
            model_name='department',
            name='location',
            field=models.CharField(blank=True, choices=[('FoH', 'Foh'), ('BoH', 'Boh')], max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='position',
            field=models.CharField(choices=[('1', 'Manager'), ('2', 'Assistant Manager'), ('3', 'Supervisor'), ('4', 'Server'), ('5', 'Busser'), ('6', 'Bartender'), ('7', 'Expo'), ('8', 'Host'), ('9', 'Barback'), ('20', 'Chef'), ('21', 'Sous Chef'), ('22', 'Pantry'), ('23', 'Line Cook'), ('24', 'Grill Cook'), ('25', 'Prep Cook'), ('26', 'Fry Cook'), ('27', 'Dishwasher')], max_length=20),
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]
