from django import forms
from django.forms import ModelForm
from .models import Employe, Departement


class EmployeForm(ModelForm):
   #ce code permet de remplacer les tirets par Département comme premier élément dans la liste.
   def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['departement'].choices = [('', 'Département')] + [(departement.code, departement.code) for departement in Departement.objects.all()]

   class Meta:
       model = Employe
       fields = ('cin','nom', 'prenom', 'date_naissance', 'sexe', 'email', 'telephone', 'adresse','titre', 'departement', 'salaire', 'date_debut_travail')
       labels = {
           'cin': '',
           'nom': '',
           'prenom': '',
           'date_naissance': '',
           'sexe': '',
           'email': '',
           'telephone': '',
           'adresse': '',
           'titre': '', 
           'departement': '',
           'salaire': '',
           'date_debut_travail' : ''
       }
       # Widgets nous permettra de styliser notre forme avec Bootstrap
       widgets = {
            'cin': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'CIN'}),
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}),
            'date_naissance': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date de Naissance'}),
            'sexe': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sexe'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse'}),
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Poste'}),
            #'departement': forms.Select(attrs={'class': 'form-control'}, choices=[('Choisissez un département')] + list(Departement.objects.values_list('code', 'code'))),
            'salaire': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Salaire'}),
            'date_debut_travail': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date debut de travail'}),
        }



class DepartementForm(ModelForm):
    class Meta:
        model = Departement
        fields = ('code','nom', 'description')
        labels = {
           'code': '',
           'nom': '',
           'description': '',
        }
       # Widgets nous permettra de styliser notre forme avec Bootstrap
        widgets={
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code'}),
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description'}),
       }



