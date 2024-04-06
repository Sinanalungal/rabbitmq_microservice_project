from django.urls import path
from . import views

from .views import ProductViewSet



urlpatterns = [
    path('coupon',ProductViewSet.as_view({'get':'list','post':'create'})),
    path('coupon/<str:pk>',ProductViewSet.as_view({'put':'update'})),
]
