from django.urls import path
from ghostpost import views

urlpatterns = [
    path('', views.index, name='home'),
]