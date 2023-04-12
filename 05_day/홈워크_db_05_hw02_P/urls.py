# accounts/urls.py

from django.urls import path
app_name = 'accounts'
urlpatterns = [
    ...
    path('<int:__(a)__>/follow/', views.follow, name='follow'),
]