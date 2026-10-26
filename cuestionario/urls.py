from django.urls import path
from .views import cuestionario

urlpatterns = [
    path('', cuestionario, name='cuestionario'),
]