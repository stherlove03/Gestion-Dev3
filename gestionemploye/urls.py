from django.urls import path
from . import views

#urlpatterns = [
   ##path('', views.index),
   #path('employe/', views.listeemploye),
#]
urlpatterns = [
   #path('admin/', admin.site.urls),
   path('employe/', views.listeemploye),
   path('', views.listeemploye),
]

##urlpatterns = [
   #path('admin/', admin.site.urls),
   #path('liste/', views.index ),
   #path('', include('gestionemploye.urls')), 
#]