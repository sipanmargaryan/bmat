from rest_framework import generics

import music.models
from .serializers import MusicSerializer

__all__ = (
    'SingleAPIView',
)


class SingleAPIView(generics.RetrieveAPIView):
    queryset = music.models.Music.objects.all()
    serializer_class = MusicSerializer
    lookup_field = 'iswc'
