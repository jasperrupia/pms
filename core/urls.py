"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from .settings import dev
from django.conf.urls.static import static 

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('dashboard.urls', namespace='dashboard')),
    path('', include('medicine.urls', namespace='medicine')),
    path('', include('sales.urls', namespace='sales')),
    path('', include('settings.urls', namespace='settings')),
    path('', include('userAuth.urls')),
    path('', include('landingPage.urls')),
] 

if dev.DEBUG:  
    urlpatterns += static(dev.MEDIA_URL,document_root=dev.MEDIA_ROOT)  
