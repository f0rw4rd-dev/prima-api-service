from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class PlayerItem:
    class Meta:
        unique_together = ('player', 'item')

    class ItemEnum(models.IntegerChoices):
        __empty__ = _('(Unknown)')

    player = models.ForeignKey('players.Player', on_delete=models.RESTRICT, verbose_name=_('Player'))
    item = models.IntegerField(choices=ItemEnum.choices, verbose_name=_('Item'))
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity'))
