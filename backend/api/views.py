from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    print('over here')
    return JsonResponse({"message": "Hi there, this is your Django API response!!"})
    