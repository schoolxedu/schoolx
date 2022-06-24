from rest_framework.generics import ListAPIView

from .models import User
from .serializers import UserSerializer


class UsersList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context


