from django.contrib.auth.decorators import login_required
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.http import Http404

from .models import Itineraire, Sortie
from .forms import SortieForm

# Create your views here.

@login_required() 
def itineraires(request):
    itineraires = get_list_or_404(Itineraire)
    return render(request, 'itineraires/itineraires.html', {'itineraires': itineraires})

@login_required() 
def sorties(request, itineraire_id):
    sorties = get_object_or_404(Sortie, pk=itineraire_id)
    return render(request, 'itineraires/sorties.html', {'sorties': sorties})


@login_required() 
def sortie(request, sortie_id):
    sortie_details = get_object_or_404(sortie_details.html, pk=sortie_id)
    return render(request, 'itineraires/sortie_details.html', {'sortie': sortie})

@login_required() 
def nouvelle_sortie(request):
    if request.method == 'GET':
        form = SortieForm()
    elif request.method == 'POST':
        form = SortieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('itineraires:itineraires')
    return render(request, 'itineraires/nouvelle_sortie.html', {'form': form})


@login_required() 
def modif_sortie(request, sortie_id):
    # il faut ajouter restriction d'utilisateur
    sortie = Sortie.objects.get(pk=sortie_id)
    if request.method == 'GET':
        form = SortieForm(instance=sortie)
    elif request.method == 'POST':
        form = SortieForm(request.POST, instance=sortie)
        if form.is_valid():
            form.save()
            return redirect('itineraires:itineraires')
    return render(request, 'itineraires/modif_sortie.html', {'form': form})
    