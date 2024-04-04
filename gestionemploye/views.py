from django.shortcuts import render
from gestionemploye.models import Employe
# Create your views here.
def index(request):
    listeemploye = Employe.objects.all()
    return render(request, 'employe/liste_employe.html', {'listeemploye': listeemploye})
