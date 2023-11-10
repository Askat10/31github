from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model
from applications.account.user.serializers import RegistrationSerializer
from rest_framework.response import Response

User = get_user_model()


class RegistrationView(CreateAPIView):
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return Response({'message': 'Thank you for registration, \
            we\'ve sent your activation code to your email address'})
