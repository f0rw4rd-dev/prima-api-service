from .models import Friends
from .serializers import FriendSerializer
from rest_framework import mixins, generics, status
from rest_framework.response import Response
from django.db.models import Q


# Create your views here.
class FriendList(mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 generics.GenericAPIView):
    queryset = Friends.objects.all()
    serializer_class = FriendSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = FriendSerializer(data=request.data)
        friend_one = request.data.get('friend_one')
        friend_two = request.data.get('friend_two')

        if serializer.is_valid() and friend_one != friend_two:
            pair_exists = Friends.objects.filter(friend_one__in=(friend_one, friend_two),
                                                 friend_two__in=(friend_one, friend_two)).exists()

            if not pair_exists:
                serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FriendDetail(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   generics.GenericAPIView):
    queryset = Friends.objects.all()
    serializer_class = FriendSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
