from django.urls import path

from . import views

app_name = 'simzam'
urlpatterns = [
    path('drodler/<slug:slug>/', views.drawing_detail, name='drawing_detail'),
    path('drodler/', views.drawing_index, name='drawing_index'),
    path('', views.index, name="home"),
]
