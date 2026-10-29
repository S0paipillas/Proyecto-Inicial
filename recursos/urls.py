from django.urls import path
from . import views

urlpatterns = [
    path("", views.recursos, name="recursos"),
    path('derechos/', views.derechos_estudiantiles, name='derechos'),
]