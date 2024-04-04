"""
URL configuration for gestion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from gestionemploye import views
#urlpatterns = [
   # path('admin/', admin.site.urls),
   # path('', include('gestionemploye.urls')),
#]
##urlpatterns = [
   #path('admin/', admin.site.urls),
   #path('liste/', views.index ),
   #path('', include('gestionemploye.urls')),
#]
urlpatterns = [
   path('admin/', admin.site.urls),
   path('employe/', views.listeemploye),
   path('', views.listeemploye),
]