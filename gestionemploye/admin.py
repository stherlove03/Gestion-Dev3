from django.contrib import admin
from .models import Employe, Departement
# Register your models here.

class affichageemploye(admin.ModelAdmin):
    list_display = ['cin','nom','prenom','date_naissance', 'sexe', 'email', 'telephone', 'adresse','titre','departement', 'salaire', 'date_debut_travail']

admin.site.register(Employe , affichageemploye)

class affichagedepartement(admin.ModelAdmin):
    list_display = ['code','nom','description']

admin.site.register(Departement, affichagedepartement)
