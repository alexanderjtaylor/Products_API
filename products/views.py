from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializer import ProductSerializer
from .models import Product
from products import serializer

# Create your views here.

@api_view('GET')
def product_list(request):
    
    products = Product.objects.all()
    
    serializer = ProductSerializer(products, many=True)
    
    
    return Response(serializer.data)