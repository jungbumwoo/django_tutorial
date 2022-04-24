from django.urls import path

from . import views

urlpatterns = [
    path('serializers', views.api_home), # localhost:8000/api/
    path('random', views.use_decorator_random),
    path('', views.use_serializer_random), 
    path('posts', views.post_random) 
]