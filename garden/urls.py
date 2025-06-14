from django.urls import path
from . import views

urlpatterns = [
    path('', views.garden_list, name='garden'),
    path('plant/<int:pk>/', views.plant_detail, name='plant_detail'),
    path('add/', views.add_plant, name='add_plant'),
    path('plant/<int:plant_id>/edit/', views.edit_plant, name='edit_plant'),
]