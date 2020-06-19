from django.urls import path

from .views import SingleAPIView

app_name = 'music'
urlpatterns = [
    path('single/<str:iswc>', SingleAPIView.as_view(), name='work'),
]
