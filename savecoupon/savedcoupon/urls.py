from django.urls import path
from . import views

from .views import ProductViewSet


urlpatterns = [
    path('saved/',ProductViewSet.as_view({'get':'list'})),
]
