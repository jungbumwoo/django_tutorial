import json
from django.http import JsonResponse

from products.models import Product

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

def api_random(request, *args, **kwargs):
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data['id'] = model_data.id 
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
    return JsonResponse(data)