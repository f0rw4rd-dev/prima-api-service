from .models import PlayerItem
from rest_framework import serializers


class PlayerItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerItem
        fields = ('player', 'item', 'quantity')
