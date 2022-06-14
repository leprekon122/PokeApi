from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='main'),
    path('accounts/', include('allauth.urls')),
    path('registration/', views.Registration.as_view(), name="reg"),
    path('pokemon_api/', views.PokemonApi.as_view(), name="api"),

]