from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class PlayerStat(models.Model):
    player = models.ForeignKey('players.Player', on_delete=models.CASCADE, verbose_name=_('Player'))
    level = models.PositiveIntegerField(verbose_name=_('Level'))
    money = models.PositiveIntegerField(verbose_name=_('Money'))
