from rest_framework.decorators import api_view
from rest_framework.response import Response # типо render
from products.serializers import ProductSerializer
from products.models import Product
from rest_framework import status

@api_view(['GET'])
def test(request):
    contex = {
        'integer':100,
        'string': 'hello world',
        'boolean': True,
        'list': [
            1, 2, 3
        ]
    }
    return Response(data=contex)

@api_view(['GET'])
def product_list_view(request):
    products = Product.objects.all()
    data = ProductSerializer(products, many=True).data
    return Response(data=data)

@api_view(['GET'])
def product_detail_view(request, id):
    try:
        product = Product.objects.get(id = id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND, data={'message': 'Product not found'})
    data = ProductSerializer(product).data
    return Response(data=data)