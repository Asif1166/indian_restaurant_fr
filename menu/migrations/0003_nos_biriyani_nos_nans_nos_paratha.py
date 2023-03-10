# Generated by Django 3.2.16 on 2023-02-09 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_alter_nos_entrées_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nos_Biriyani',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('item_type', models.CharField(default='Entrées', max_length=30)),
                ('description', models.TextField(max_length=300)),
                ('price', models.FloatField()),
                ('thumbnail', models.ImageField(upload_to='media/menu')),
            ],
        ),
        migrations.CreateModel(
            name='Nos_Nans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('item_type', models.CharField(default='Entrées', max_length=30)),
                ('description', models.TextField(max_length=300)),
                ('price', models.FloatField()),
                ('thumbnail', models.ImageField(upload_to='media/menu')),
            ],
        ),
        migrations.CreateModel(
            name='Nos_Paratha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('item_type', models.CharField(default='Entrées', max_length=30)),
                ('description', models.TextField(max_length=300)),
                ('price', models.FloatField()),
                ('thumbnail', models.ImageField(upload_to='media/menu')),
            ],
        ),
    ]
