from .models import PlayerExpansion
from rest_framework import serializers


class PlayerExpansionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlayerExpansion
        fields = ('player', 'expansion')
