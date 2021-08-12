# Django
from django.contrib import admin
from django.urls import path, include

# Views
from clients.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clients/', include('clients.urls')),
    path('', home, name='home')
]
