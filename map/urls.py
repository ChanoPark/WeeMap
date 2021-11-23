from django.urls import path
from map import views

urlpatterns = [
    path('render/', views.rendering_map),
    path('registerbooth/', views.register_booth),
    path('deletebooth/', views.delete_booth),
]