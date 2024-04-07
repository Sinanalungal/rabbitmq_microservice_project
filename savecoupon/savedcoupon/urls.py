from django.urls import path
from . import views

from .views import ProductViewSet
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('saved/',ProductViewSet.as_view({'get':'list'})),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)