from django.urls import path

from . import views

app_name = 'simzam'
urlpatterns = [
    path('', views.index, name="home"),
    path('tegning/<uuid:uuid>/', views.drawing_detail, name='drawing_detail'),
]

htmx_urlpatterns = [

]

urlpatterns += htmx_urlpatterns
