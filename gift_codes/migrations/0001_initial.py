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
            name='GiftCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hashed_code', models.CharField(max_length=256, unique=True, verbose_name='Hashed code')),
                ('activation_count', models.PositiveIntegerField(verbose_name='Activation count')),
                ('category', models.IntegerField(choices=[(None, '(Unknown)'), (1, 'Item'), (2, 'Cosmetic'), (3, 'Expansion'), (4, 'Money'), (5, 'Level')], verbose_name='Category')),
                ('gift', models.IntegerField(verbose_name='Gift')),
                ('quantity', models.PositiveIntegerField(verbose_name='Quantity')),
            ],
        ),
        migrations.CreateModel(
            name='GiftCodeUsage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usage_time', models.DateTimeField(auto_now_add=True, verbose_name='Usage time')),
                ('gift_code', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='gift_codes.giftcode', verbose_name='Gift code')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='players.player', verbose_name='Player')),
            ],
            options={
                'unique_together': {('player', 'gift_code')},
            },
        ),
    ]