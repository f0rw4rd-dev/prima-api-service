from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Player(models.Model):
    class PlatformType(models.IntegerChoices):
        STEAM = 1, _('Steam')
        EPIC_GAMES = 2, _('Epic Games')
        MICROSOFT_STORE = 3, _('Microsoft Store')
        XBOX = 4, _('Xbox')
        PLAYSTATION = 5, _('PlayStation')

        __empty__ = _("(Unknown)")

    personal_key = models.CharField(max_length=9, unique=True, verbose_name=_('Personal key'))
    platform = models.IntegerField(choices=PlatformType.choices, verbose_name=_('Platform'))
    first_join_time = models.DateTimeField(verbose_name=_('First join time'))
    last_join_time = models.DateTimeField(verbose_name=_('Last join time'))
    total_hours = models.PositiveIntegerField(verbose_name=_('Total hours'))
