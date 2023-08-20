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
            name='PlayerStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_stat', models.IntegerField(choices=[(None, '(Unknown)'), (1, 'Money'), (2, 'Level')], verbose_name='Player stat')),
                ('value', models.CharField(max_length=256, verbose_name='Value')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='players.player', verbose_name='Player')),
            ],
            options={
                'unique_together': {('player', 'player_stat')},
            },
        ),
    ]