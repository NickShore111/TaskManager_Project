# Generated by Django 3.2.7 on 2021-10-21 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='attendance',
            field=models.IntegerField(choices=[(1, 'Unacceptable'), (2, 'Needs Improvement'), (3, 'Satisfactory'), (4, 'Above Average'), (5, 'Exceptional')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='attire',
            field=models.IntegerField(choices=[(1, 'Unacceptable'), (2, 'Needs Improvement'), (3, 'Satisfactory'), (4, 'Above Average'), (5, 'Exceptional')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='customer_service',
            field=models.IntegerField(choices=[(1, 'Unacceptable'), (2, 'Needs Improvement'), (3, 'Satisfactory'), (4, 'Above Average'), (5, 'Exceptional')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='grooming',
            field=models.IntegerField(choices=[(1, 'Unacceptable'), (2, 'Needs Improvement'), (3, 'Satisfactory'), (4, 'Above Average'), (5, 'Exceptional')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='initiative',
            field=models.IntegerField(choices=[(1, 'Unacceptable'), (2, 'Needs Improvement'), (3, 'Satisfactory'), (4, 'Above Average'), (5, 'Exceptional')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='performance',
            field=models.IntegerField(choices=[(1, 'Unacceptable'), (2, 'Needs Improvement'), (3, 'Satisfactory'), (4, 'Above Average'), (5, 'Exceptional')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='punctuality',
            field=models.IntegerField(choices=[(1, 'Unacceptable'), (2, 'Needs Improvement'), (3, 'Satisfactory'), (4, 'Above Average'), (5, 'Exceptional')]),
        ),
        migrations.AlterField(
            model_name='review',
            name='teamwork',
            field=models.IntegerField(choices=[(1, 'Unacceptable'), (2, 'Needs Improvement'), (3, 'Satisfactory'), (4, 'Above Average'), (5, 'Exceptional')]),
        ),
    ]