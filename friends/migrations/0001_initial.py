# Generated by Django 4.2.4 on 2023-08-19 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('friend_one', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='friend_one_set', to='players.player', verbose_name='Friend 1')),
                ('friend_two', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='friend_two_set', to='players.player', verbose_name='Friend 2')),
            ],
            options={
                'unique_together': {('friend_one', 'friend_two')},
            },
        ),
    ]