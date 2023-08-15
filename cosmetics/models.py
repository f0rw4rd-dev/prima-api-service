from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Cosmetic(models.Model):
    class CosmeticType(models.IntegerChoices):
        __empty__ = _("(Unknown)")

    player = models.ForeignKey('players.Player', on_delete=models.CASCADE, verbose_name=_('Player'))
    cosmetic = models.IntegerField(choices=CosmeticType.choices, verbose_name=_('Cosmetic'))
