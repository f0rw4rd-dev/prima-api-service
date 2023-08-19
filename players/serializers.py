from .models import Player
from rest_framework import serializers


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = ('personal_key', 'platform', 'first_join_time', 'last_join_time', 'total_hours')
