from rest_framework import viewsets
from knox.views import LoginView as KnoxLoginView
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer
from .models import CustomUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class LoginView(KnoxLoginView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_post_response_data(self, request, token, instance):
        data = {
            'expiry': self.format_expiry_datetime(instance.expiry),
            'token': token
        }
        if UserSerializer is not None:
            data['user'] = UserSerializer(request.user, context=self.get_context()).data
        return data