import json
from django.http import JsonResponse

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