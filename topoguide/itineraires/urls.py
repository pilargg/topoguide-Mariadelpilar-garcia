from django.urls import path

from . import views

app_name = 'itineraires'

urlpatterns = [
    path('', views.itineraires, name='itineraires'),
    path('sorties/<int:itineraire_id>/', views.sorties, name='sorties'),
    path('sortie/<int:sortie_id>/', views.sortie, name='sortie'),
    path('nouvelle_sortie/', views.nouvelle_sortie, name='nouvelle_sortie'),
    path('modif_sortie/<int:sortie_id>/', views.modif_sortie, name='modif_sortie'),
]