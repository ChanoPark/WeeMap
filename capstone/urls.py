from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', obtain_jwt_token),
    path('auth/verify', verify_jwt_token),
    path('auth/refresh', refresh_jwt_token),
    path('account/', include('account.urls')),
    path('tab/', include('tab.urls')),
    path('map/', include('map.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)