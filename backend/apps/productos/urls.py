from django.urls import path
from . import views

urlpatterns = [
    path('<int:tienda_id>/', views.lista_productos, name='lista_productos'),
]
