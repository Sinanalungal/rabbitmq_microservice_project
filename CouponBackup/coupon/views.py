from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.views import APIView
from .producer import publish
from .models import Product
from .serializer  import ProductSerializer
# from .producer import publish
from django.http import HttpResponse


# from products.task import consume_rabbitmq_messages
# from products.task import produce_message_to_rabbitmq 
# from django.http import HttpResponse


class ProductViewSet(viewsets.ViewSet):
    def list(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    
    def create(self,request):
        serializer=ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer)
        publish(serializer.data)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None):
        product = Product.objects.get(couponcode=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish(serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)



