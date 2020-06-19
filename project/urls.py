from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.conf import settings
from django.contrib import admin
from django.urls import path, include


schema_view = get_schema_view(
   openapi.Info(
      title=f'bmat API',
      default_version='v1',
      description="Bmat",
   ),
   public=True,
)


urlpatterns = [
    path(f'api/v{settings.API_VERSION}/music/', include('music.urls', namespace='music')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        path('api-docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ]
