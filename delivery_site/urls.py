"""delivery_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include
from delivery_site.views import join
from order_app.views import basket

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board_app.urls')),
    path('store/', include('store_app.urls')),
    path('basket/', basket, name='basket'),
    path('order/', include('order_app.urls')),
    path('account/', include('django.contrib.auth.urls')),
    path('account/join', join, name='join'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)