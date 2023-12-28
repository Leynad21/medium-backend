from .serializers import UserSerializer, CustomRegisterSerializer
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model


class CustomUserDetailsView(RetrieveUpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return get_user_model().objects.none()