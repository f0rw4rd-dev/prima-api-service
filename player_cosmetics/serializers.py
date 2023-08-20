from .models import PlayerCosmetic
from rest_framework import serializers


class PlayerCosmeticSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerCosmetic
        fields = ('player', 'cosmetic')
