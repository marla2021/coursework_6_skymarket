from rest_framework import pagination, viewsets

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    pass


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

    def get_serializer_class(self):
        if self.action in ["retrieve", "create", "update", "partial_update", "destroy"]:
            return AdDetailSerializer
        return AdSerializer

    # def get_permissions(self):
    #     permission_classes = (AllowAny,)
    #     if self.action in ["retrieve"]:
    #         permission_classes = (AllowAny,)
    #     elif self.action in ["create", "update", "partial_update", "destroy", "me"]:
    #         permission_classes = (IsOwner | IsAdmin,)
    #     return tuple(permission() for permission in permission_classes)

    def get_queryset(self):
        if self.action == "me":
            return Ad.objects.filter(author=self.request.user).all()
        return Ad.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

