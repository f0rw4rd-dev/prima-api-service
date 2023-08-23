from .models import PlayerCosmetic
from .serializers import PlayerCosmeticSerializer
from rest_framework import mixins, generics


# Create your views here.
class PlayerCosmeticList(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          generics.GenericAPIView):
    queryset = PlayerCosmetic.objects.all()
    serializer_class = PlayerCosmeticSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PlayerCosmeticDetail(mixins.RetrieveModelMixin,
                            mixins.UpdateModelMixin,
                            mixins.DestroyModelMixin,
                            generics.GenericAPIView):
    queryset = PlayerCosmetic.objects.all()
    serializer_class = PlayerCosmeticSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
