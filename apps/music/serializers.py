from rest_framework import serializers

import music.models

__all__ = (
    'MusicSerializer',
)


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = music.models.Music
        fields = '__all__'
