from rest_framework import generics
from .models import Performer
from .serializers import PerformerListSerializer


class PerformerListView(generics.ListAPIView):
    queryset = Performer.objects.all()
    serializer_class = PerformerListSerializer
