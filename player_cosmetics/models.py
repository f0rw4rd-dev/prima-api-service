from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class PlayerCosmetic(models.Model):
    class Meta:
        unique_together = ('player', 'cosmetic')

    class CosmeticEnum(models.IntegerChoices):
        __empty__ = _('(Unknown)')

    player = models.ForeignKey('players.Player', on_delete=models.RESTRICT, verbose_name=_('Player'))
    cosmetic = models.IntegerField(choices=CosmeticEnum.choices, verbose_name=_('Cosmetic'))
