"""bembos_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('bembos/', include('bembos.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from apps.bembos.urls import router
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView #una para obtener el token y otra para refrescarlo

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('', include('apps.bembos.urls')),

    path('api/',include(router.urls)),

    path('api-auth', include('rest_framework.urls')), #para crear el login y no depender del admin
    path('api/token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/refresh', TokenRefreshView.as_view(), name='token_refresh') #probarlo en postman 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
