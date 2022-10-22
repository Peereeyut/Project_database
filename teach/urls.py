from django.urls import path
from .views import testing
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('course/', testing )
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)