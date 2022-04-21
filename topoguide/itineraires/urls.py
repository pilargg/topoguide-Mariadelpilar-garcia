from django.urls import path

from . import views

app_name = 'itineraires'

urlpatterns = [
    path('', views.itineraires, name='itineraires'),
    path('sortie/<int:itineraire_id>/', views.sorties, name='sorties'),
    path('sortie/<int:sortie_id>/', views.sortie, name='sortie_details'),
    path('sortie/nouvelle_sortie/', views.nouvelle_sortie, name='nouvelle_sortie'),
    path('sortie/modif_sortie/<int:sortie_id>/', views.modif_sortie, name='modif_sortie'),
]