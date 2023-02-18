from django.urls import path

from . import views

app_name = 'simzam'

urlpatterns = [
    path('test', views.detail, name='test'),
]
