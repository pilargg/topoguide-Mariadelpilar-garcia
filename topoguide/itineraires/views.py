from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Itineraire, Sortie
from .forms import SortieForm

# Create your views here.


def itineraires(request):
    itineraires = get_list_or_404(Itineraire)
    return render(request, 'itineraires/itineraires.html', {'itineraires': itineraires})

def sorties(request):
    sorties = get_list_or_404(Sortie)
    return render(request, 'itineraires/sorties.html', {'sorties': sorties})

def sortie(request):
    sortie_details = get_object_or_404(sortie_details.html, pk=sortie_id)
    return render(request, 'itineraires/sortie_details.html', {'sortie': sortie})

def nouvelle_sortie(request):
    if request.method == 'GET':
        form = SortieForm()
    elif request.method == 'POST':
        form = SortieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('itineraires:sorties')
    return render(request, 'itineraires/nouvelle_sortie.html', {'form': form})

def modif_sortie(request):
    # il faut ajouter restriction d'utilisateur
    sortie = Sortie.objects.get(pk=sortie_id)
    if request.method == 'GET':
        form = SortieForm(instance=sortie)
    elif request.method == 'POST':
        form = SortieForm(request.POST, instance=sortie)
        if form.is_valid():
            form.save()
            return redirect('itineraires:sorties')
    return render(request, 'itineraires/modif_sortie.html', {'form': form})
    