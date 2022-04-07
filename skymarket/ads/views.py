from rest_framework import pagination, viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from ads.models import Ad, Comment
from ads.permissions import IsOwner, IsAdmin
from ads.serializers import AdSerializer, AdDetailSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


# TODO view функции. Предлагаем Вам следующую структуру - но Вы всегда можете использовать свою
class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


    def get_permissions(self):
        permission_class = (AllowAny, )
        if self.action != "retrieve":
            permission_class = (IsOwner|IsAdmin)
        return tuple(permission() for permission in permission_class)


    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

    def get_serializer_class(self):
        if self.action in ["retrieve", "create", "update", "partial_update", "destroy"]:
            return AdDetailSerializer
        return AdSerializer


    def get_queryset(self):
        if self.action == "me":
            return Ad.objects.filter(author=self.request.user).all()
        return Ad.objects.all()


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_permissions(self):
        permission_class = (IsAuthenticated, )
        if self.action not in ["retrieve", "list"]:
            permission_class = (IsOwner|IsAdmin)
        return tuple(permission() for permission in permission_class)