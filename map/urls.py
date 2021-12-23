from django.urls import path
from map import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('render/', views.rendering_map),
    path('registerbooth/', views.register_booth),
    path('deletebooth/', views.delete_booth),
    path('markerinfo/', views.marker_info),
    path('hotplace/', views.cal_hotplace),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)