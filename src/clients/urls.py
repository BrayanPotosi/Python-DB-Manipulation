# Django
from django.urls import path

# Views
from .views import list_clients, list_products, delete_client, add_client, add_product, delete_product

urlpatterns = [
    path('clients/', list_clients, name='clients'),
    path('clients/create', add_client, name='create_client'),
    path('clients/delete', delete_client, name='delete_client'),
    path('products/', list_products, name='products'),
    path('products/create', add_product, name='create_product'),
    path('products/delete', delete_product, name='delete_product')
]
