from django.urls import path

from . import views

app_name = 'simzam'
urlpatterns = [
    path('', views.DrawingList.as_view(), name="drawings"),
    path('tegning/<uuid:uuid>/', views.DrawingDetailView.as_view(), name='drawing'),
]

htmx_urlpatterns = [

]

urlpatterns += htmx_urlpatterns
