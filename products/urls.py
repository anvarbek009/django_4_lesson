from django.urls import path
from .views import get_info, get_products, detail, add_products, update_products, delete_products, search_products

app_name = 'products'
urlpatterns = [
    path('', get_info, name='get_info'),
    path('products/<int:pk>', get_products, name='get_products'),
    path('products/detail/<int:pk>', detail, name='detail'),
    path('add_products', add_products, name='add_products'),
    path('update/<int:pk>', update_products, name='update_products'),
    path('delete/<int:pk>', delete_products, name='delete_products'),
    path('search', search_products, name='search_products'),
]
