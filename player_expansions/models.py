from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class PlayerExpansion(models.Model):
    class Meta:
        unique_together = ('player', 'expansion')

    class ExpansionEnum(models.IntegerChoices):
        __empty__ = _('(Unknown)')

    player = models.ForeignKey('players.Player', on_delete=models.RESTRICT, verbose_name=_('Player'))
    expansion = models.IntegerField(choices=ExpansionEnum.choices, verbose_name=_('Expansion'))
