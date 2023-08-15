from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Extension(models.Model):
    class ExtensionType(models.IntegerChoices):
        __empty__ = _("(Unknown)")

    player = models.ForeignKey('players.Player', on_delete=models.CASCADE, verbose_name=_('Player'))
    extension = models.IntegerField(choices=ExtensionType.choices, verbose_name=_('Extension'))
