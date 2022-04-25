from django.urls import path

from . import views

urlpatterns = [
    path('create/', views.ProductCreateAPIView.as_view()),
    path('create/list/', views.ProductListCreateAPIView.as_view()),
    path('showlist/', views.ProductListAPIView.as_view()),
    path('<int:pk>/', views.product_detail_view), # ProductDetailAPIView.as_view()
]