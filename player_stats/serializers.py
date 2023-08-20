from .models import PlayerStat
from rest_framework import serializers


class PlayerStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerStat
        fields = ('player', 'player_stat', 'value')
