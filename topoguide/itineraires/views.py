from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Itineraire, Sortie

# Create your views here.


def itineraires(request):
    itineraires = get_list_or_404(Itineraire)
    return render(request, 'itineraires/itineraires.html', {'itineraires': itineraires})

def sorties(request):
    sorties = get_list_or_404(Sortie)
    return render(request, 'sorties/sorties.html', {'sorties': sorties})

# def sortie(request):
#     sortie_details = get_object_or_404(sortie_details.html, pk=sortie_id)
#     return render(request, 'sorties/sortie_details.html', {'sortie': sortie})
    