from rest_framework import generics
from .serializer import SnackSerializer
from .models import Snack
from .permissions import IsOwnerOrReadOnly

class SnackList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer

class SnackDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Snack.objects.all()
    serializer_class = SnackSerializer
