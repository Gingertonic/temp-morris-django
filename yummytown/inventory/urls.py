from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inventory-index'),
    path('about/', views.about, name='inventory-how-to'),
    path('<int:id>/', views.show, name='show-item'),
    path('new/', views.create, name='create-item')
]