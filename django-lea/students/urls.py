from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.index, name='index'),
    path('add-student/', views.addStudent, name='add'),
    path('about/', views.aboutUs, name='add'),
]
