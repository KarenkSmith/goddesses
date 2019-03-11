from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('gods/', views.gods_index, name="index"),
    path('gods/<int:god_id>/', views.gods_detail, name='detail'),
]