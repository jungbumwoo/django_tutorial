import json
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True): # raise exception 추가함으로서 에러를 보다 잘 파악할 수 있게 return 됨
        instance = serializer.save()
        print(instance)
        return Response(serializer.data)