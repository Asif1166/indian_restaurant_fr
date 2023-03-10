# Generated by Django 3.2.16 on 2023-02-09 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='closing_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='day',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='location',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='opening_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
    ]
