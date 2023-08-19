from django.db import models
from django.utils.translation import gettext as _


# Create your models here.
class Friends(models.Model):
    class Meta:
        unique_together = ('friend_one', 'friend_two')

    friend_one = models.ForeignKey('players.Player', on_delete=models.RESTRICT, verbose_name=_('Friend 1'))
    friend_two = models.ForeignKey('players.Player', on_delete=models.RESTRICT, verbose_name=_('Friend 2'))
