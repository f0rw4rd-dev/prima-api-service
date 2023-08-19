from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class PlayerStat(models.Model):
    class Meta:
        unique_together = ('player', 'player_stat')

    class PlayerStatEnum(models.IntegerChoices):
        MONEY = 1, _('Money')
        LEVEL = 2, _('Level')

        __empty__ = _('(Unknown)')

    player = models.ForeignKey('players.Player', on_delete=models.RESTRICT, verbose_name=_('Player'))
    player_stat = models.IntegerField(choices=PlayerStatEnum.choices, verbose_name=_('Player stat'))
    value = models.CharField(max_length=256, verbose_name=_('Value'))
