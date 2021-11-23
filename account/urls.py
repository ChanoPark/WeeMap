from django.urls import path
from account import views

urlpatterns = [
    path('register/', views.register),
    path('logout/', views.logout),
    path('info/', views.info),
]