from django.shortcuts import render
from rest_framework import viewsets,status
from rest_framework.response import Response
from .models import Product
from .serializer  import ProductSerializer


class ProductViewSet(viewsets.ViewSet):
    def list(self,request):
        products = Product.objects.filter(redeemed=True).all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    
