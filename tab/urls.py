from django.urls import path
from tab import views

urlpatterns = [
    path('weekbus/', views.getBus),
    path('restaurant/', views.getMenu),
]