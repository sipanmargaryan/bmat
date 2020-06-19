from django.db import models


__all__ = (
    'Music',
)


class Music(models.Model):
    title = models.CharField(max_length=80)
    contributors = models.CharField(max_length=250)
    iswc = models.CharField(max_length=30, unique=True)

    class Meta:
        indexes = [
            models.Index(fields=['iswc']),
        ]

    def __str__(self):
        return self.iswc

