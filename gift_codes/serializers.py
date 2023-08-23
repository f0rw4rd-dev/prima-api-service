from .models import GiftCode, GiftCodeUsage
from rest_framework import serializers


class GiftCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftCode
        fields = ('code', 'activation_count', 'category', 'gift', 'quantity')


class GiftCodeUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GiftCodeUsage
        fields = ('player', 'gift_code', 'usage_time')
