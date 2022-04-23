import json
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from requests import Response
from django.http import JsonResponse

from products.models import Product
from products.serializers import ProductSerializer


def api_home(request, *args, **kwargs):
    body = request.body # byte string of JSON data
    data = {}
    try:
        data = json.loads(body) # string of JSON data -> Python Dictionary
    except:
        pass

    print('data: {}'.format(data)) # empty
    print('request.GET: {}'.format(request.GET))

    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)

def random_send_modelToDict_and_Http(request, *args, **kwargs):
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data['id'] = model_data.id 
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
    return JsonResponse(data)

def api_random(request, *args, **kwargs):
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
        json_data_str = json.dumps(data)
    return JsonResponse(json_data_str)

@api_view(["GET"])
def use_decorator_random(request, *args, **kwargs):
    '''
    DEF API View
    '''
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price', 'sale_price'])
    return JsonResponse(data)

@api_view(["GET"])
def use_serializer_random(request, *args, **kwargs):
    '''
    DEF API View
    '''
    print('here')
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data = model_to_dict(instance, fields=['id', 'title', 'price', 'sale_price'])
        print('ㄱ. ProductSerializer(instance) at func use_serializer_random :은 {}'.format(ProductSerializer(instance)))
        data = ProductSerializer(instance).data
    return JsonResponse(data)