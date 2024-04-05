from django.urls import path
from . import views


urlpatterns = [
   #path('admin/', admin.site.urls),
   path('employe/', views.listeemploye),
   path('', views.listeemploye),
   path('modifier_employe/<int:employe_id>', views.modifier_employe, name='modifier-employe'),
]
