# Generated by Django 3.2.16 on 2023-02-09 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20230209_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='About_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('sub_title', models.CharField(blank=True, max_length=300, null=True)),
                ('point1', models.CharField(blank=True, max_length=100, null=True)),
                ('point2', models.CharField(blank=True, max_length=100, null=True)),
                ('point3', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('picture', models.ImageField(upload_to='media/about_us')),
            ],
        ),
    ]
