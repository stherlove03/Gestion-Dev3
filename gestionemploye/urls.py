from django.urls import path
from . import views
from django.urls import path

urlpatterns = [
   # Pour la page d'Accueil
   path('', views.home, name='home'),
   # Pour Afficher la liste des employes et departements
   path('liste_employe/', views.listeemploye, name='liste-employe'),
   path('liste_departement/', views.listedepartement, name='liste-departement'),

   # Pour Ajouter un enregistrement utilisant une forme
   path('ajouter_employe/', views.ajouter_employe, name='ajouter-employe'),
   path('ajouter_departement/', views.ajouter_departement, name='ajouter-departement'),
   
   # Pour Modifier un enregistrement utilisant une forme
   path('modifier_employe/<int:cin>/', views.modifier_employe, name='modifier-employe'),
   path('modifier_departement/<str:code>/', views.modifier_departement, name='modifier-departement'),
   
   # Pour Afficher un seul et unique enregistrement sans une page
   path('afficher_un_employe/<int:cin>/', views.afficher_un_employe, name='un-employe'),
   path('afficher_un_departement/<str:code>/', views.afficher_un_departement, name='un-departement'),
   
   # pour supprimer un enregistrement
   path('supprimer_un_employe/<int:cin>/', views.supprimer_un_employe, name='supprimer-employe'),
   path('supprimer_un_departement/<str:code>/', views.supprimer_un_departement, name='supprimer-departement'),
]
