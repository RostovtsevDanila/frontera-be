from rest_framework import authentication, permissions, viewsets

from frontera.serializers import LanguageSerializer


class LanguageView(viewsets.ModelViewSet):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    action_serializers = {
        'list': LanguageSerializer,
    }

    def get_serializer_class(self):
        return self.action_serializers.get(
            self.action,
            self.serializer_class
        )
