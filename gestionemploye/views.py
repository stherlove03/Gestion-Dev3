from django.shortcuts import render
from .models import Employe, Departement, Travailler
from django.views.decorators.csrf import csrf_protect
from .forms import EmployeForm, DepartementForm
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
# Create your views here.

def home(request):
    return render(request, 'employe/home.html')

def listeemploye(request):
   employe = Employe.objects.all()
   return render(request, 'employe/liste_employe.html', {'employe': employe})

def listedepartement(request):
   departement = Departement.objects.all()
   return render(request, 'employe/liste_departement.html', {'departement': departement})

@csrf_protect

def ajouter_employe(request):
   submitted = False
   if request.method == 'POST':
       form = EmployeForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect('/ajouter_employe?submitted=True')
   else:
       form = EmployeForm()
       if 'submitted' in request.GET:
           submitted = True
   return render(request, 'employe/ajouter_un_employe.html', {'form':form, 'submitted':submitted})


def ajouter_departement(request):
   submitted = False
   if request.method == 'POST':
       form = DepartementForm(request.POST)
       if form.is_valid():
           form.save()
           return HttpResponseRedirect('/ajouter_departement?submitted=True')
   else:
       form = DepartementForm()
       if 'submitted' in request.GET:
           submitted = True
   return render(request, 'employe/ajouter_departement.html', 
{'form':form, 'submitted':submitted})




def modifier_employe(request, cin):
    employe= Employe.objects.get(pk=cin)
    form = EmployeForm(request.POST or None, instance=employe)
    if form.is_valid():
        form.save()
        return redirect('liste-employe')
    return render(request, 'employe/modifier_un_employe.html', {'employe': employe, 'form': form})

def modifier_departement(request, code):
    departement= Departement.objects.get(pk=code)
    form = DepartementForm(request.POST or None, instance=departement)
    if form.is_valid():
        form.save()
        return redirect('liste-departement')
    return render(request, 'employe/modifier_departement.html', {'departement': departement, 'form': form})

def afficher_un_employe(request, cin):
    employe = Employe.objects.get(pk=cin)
    return render(request, 'employe/afficher_un_employe.html', {'employe': employe})

def afficher_un_departement(request, code):
    departement = Departement.objects.get(pk=code)
    return render(request, 'employe/afficher_un_departement.html', {'departement': departement})

def supprimer_un_employe(request, cin):
    travailler = Travailler.objects.get(pk=cin)
    employe = Employe.objects.get(pk=cin)
    travailler.delete()
    employe.delete()
    return redirect('liste-employe')

def supprimer_un_departement(request, code):
    departement = Departement.objects.get(pk=code)
    departement.delete()
    return redirect('liste-departement')




