from django.urls import path
from . import views

urlpatterns = [
    path('', views.garden_list, name='garden'),
    path('plant/<int:pk>/', views.plant_detail, name='plant_detail'),
    path('add/', views.add_plant, name='add_plant'),
    path('plant/<int:plant_id>/edit/', views.edit_plant, name='edit_plant'),
    path('plant/<int:plant_id>/delete/', views.delete_plant, name='delete_plant'),
    path('photo/<int:photo_id>/delete/', views.delete_photo, name='delete_photo'),
]