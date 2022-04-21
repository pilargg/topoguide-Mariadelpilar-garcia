from django.urls import path

from . import views

app_name = 'itineraires'

urlpatterns = [
    path('', views.itineraires, name='itineraires'),
    path('sortie/<int:itineraire_id>/', views.sorties, name='sorties'),
    # path('sortie/<int:sortie_id>/', views.sortie_details, name='sortie_details'),
]