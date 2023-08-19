from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class GiftCode(models.Model):
    class GiftCategoryEnum(models.IntegerChoices):
        ITEM = 1, _('Item')
        COSMETIC = 2, _('Cosmetic')
        EXPANSION = 3, _('Expansion')
        MONEY = 4, _('Money')
        LEVEL = 5, _('Level')

        __empty__ = _('(Unknown)')

    hashed_code = models.CharField(max_length=256, unique=True, verbose_name=_('Hashed code'))
    activation_count = models.PositiveIntegerField(verbose_name=_('Activation count'))
    category = models.IntegerField(choices=GiftCategoryEnum.choices, verbose_name=_('Category'))
    gift = models.IntegerField(verbose_name=_('Gift'))
    quantity = models.PositiveIntegerField(verbose_name=_('Quantity'))


class GiftCodeUsage(models.Model):
    class Meta:
        unique_together = ('player', 'gift_code')

    player = models.ForeignKey('players.Player', on_delete=models.RESTRICT, verbose_name=_('Player'))
    gift_code = models.ForeignKey('gift_codes.GiftCode', on_delete=models.RESTRICT, verbose_name=_('Gift code'))
    usage_time = models.DateTimeField(auto_now_add=True, verbose_name=_('Usage time'))
