from django.urls import path
from .views import PokemonList, PokemonDetail

urlpatterns = [
  path('', PokemonList.as_view(), name='poke_list'),
  path('<int:pk>/', PokemonDetail.as_view(), name='poke_detail'),
]