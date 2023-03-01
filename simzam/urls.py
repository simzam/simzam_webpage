from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'simzam'
urlpatterns = [
    path('drodler/<slug:slug>/', views.drawing_detail, name='drawing_detail'),
    path('drodler/', views.drawing_index, name='drawing_index'),
    path('memo/', views.memo, name='memo'),
    path('', views.detail, name='test'),
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
