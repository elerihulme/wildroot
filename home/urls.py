from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('trigger-404/', views.trigger_404, name='trigger_404'),
]