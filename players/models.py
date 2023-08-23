from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Player(models.Model):
    class PlatformEnum(models.IntegerChoices):
        STEAM = 1, _('Steam')
        EPIC_GAMES = 2, _('Epic Games')
        MICROSOFT_STORE = 3, _('Microsoft Store')
        XBOX = 4, _('Xbox')
        PLAYSTATION = 5, _('PlayStation')

        __empty__ = _('(Unknown)')

    personal_key = models.CharField(max_length=9, unique=True, verbose_name=_('Personal key'))
    machine_key = models.CharField(max_length=256, verbose_name=_('Machine key'))
    platform = models.IntegerField(choices=PlatformEnum.choices, verbose_name=_('Platform'))
    platform_uid = models.CharField(max_length=128, unique=True, verbose_name=_('Platform uid'))

    def __str__(self):
        return self.personal_key
