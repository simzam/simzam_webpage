from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'simzam'

urlpatterns = [
    path('', views.detail, name='test'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
