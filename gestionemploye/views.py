from django.shortcuts import render
from .models import Employe
# Create your views here.


def listeemploye(request):
   listeemploye = Employe.objects.all()
   return render(request, 'employe/liste_employe.html', {'listeemploye': listeemploye})

modifier_employe