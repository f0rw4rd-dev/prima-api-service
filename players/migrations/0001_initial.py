# Generated by Django 4.2.4 on 2023-08-23 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personal_key', models.CharField(max_length=9, unique=True, verbose_name='Personal key')),
                ('machine_key', models.CharField(max_length=256, unique=True, verbose_name='Machine key')),
                ('platform', models.IntegerField(choices=[(None, '(Unknown)'), (1, 'Steam'), (2, 'Epic Games'), (3, 'Microsoft Store'), (4, 'Xbox'), (5, 'PlayStation')], verbose_name='Platform')),
                ('platform_uid', models.CharField(max_length=128, unique=True, verbose_name='Platform uid')),
                ('first_join_time', models.DateTimeField(verbose_name='First join time')),
                ('last_join_time', models.DateTimeField(verbose_name='Last join time')),
                ('total_hours', models.PositiveIntegerField(verbose_name='Total hours')),
            ],
        ),
    ]
