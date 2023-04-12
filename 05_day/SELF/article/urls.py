from django.contrib import admin
from django.urls import path
from . import views

app_name='article'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('update/', views.update, name='update'),
]