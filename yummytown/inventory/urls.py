from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='inventory-index'),
    path('about/', views.about, name='inventory-how-to'),
    path('<int:id>/', views.show, name='show-item')
]