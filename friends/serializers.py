from .models import Friends
from rest_framework import serializers


class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friends
        fields = ('friend_one', 'friend_two')
