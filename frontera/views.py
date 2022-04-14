from rest_framework import authentication, permissions, viewsets

from frontera.models import Language, Category
from frontera.serializers import LanguageSerializer, CategorySerializer


class PermissionMixin:
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class LanguageView(viewsets.ModelViewSet, PermissionMixin):
    action_serializers = {
        'list': LanguageSerializer,
    }

    def get_serializer_class(self):
        return self.action_serializers.get(
            self.action,
            self.serializer_class
        )

    def get_queryset(self):
        return Language.objects.all()


class CategoryView(viewsets.ModelViewSet, PermissionMixin):
    action_serializers = {
        'list': CategorySerializer
    }

    def get_serializer_class(self):
        return self.action_serializers.get(
            self.action,
            self.serializer_class
        )

    def get_queryset(self):
        return Category.objects.all()
