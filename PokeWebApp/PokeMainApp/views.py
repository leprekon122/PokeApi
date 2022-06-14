from django.shortcuts import render, redirect
from rest_framework import generics, mixins
from .models import *
from .forms import *
from .serializers import *
from django.contrib.auth import authenticate, login
from django.contrib import messages
import requests


# Create your views here.

class MainPage(generics.GenericAPIView):

    @staticmethod
    def get(request):

        if request.GET.get('logins'):
            try:
                username = request.GET.get('username')
                password = request.GET.get('password')

                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('main')

            except Exception:
                return redirect('main')

        username = request.user
        model = PokemonInfo.objects.all()
        user_poc = UserPokemons.objects.filter(user_name=username).values('pokemon_name__name', 'user_name', 'id')
        data = {'model': model,
                'username': username,
                'user_poc': user_poc}
        return render(request, 'PokeMainApp/main_page.html', data)

    @staticmethod
    def post(request):

        add_pokemon = request.POST.get('add_pokemon')
        del_poc = request.POST.get('del_poc')
        add_data = request.POST.get('add_data')

        if add_data:
            req = requests.get(url='https://pokeapi.co/api/v2/pokemon?offset=20&limit=1126')
            res = req.json()['results']
            item = len(PokemonInfo.objects.all().values())
            if item == 0:
                for el in res:
                    PokemonInfo.objects.create(name=el['name'], detail_url=el['url'])
                return redirect('main')
            else:
                return redirect('main')

        if add_pokemon:
            username = request.user
            UserPokemons.objects.create(user_name=username, pokemon_name=PokemonInfo(add_pokemon))
            return redirect('main')

        if del_poc:
            UserPokemons.objects.filter(id=del_poc).delete()
            return redirect('main')


class Registration(generics.GenericAPIView,
                   mixins.CreateModelMixin):

    @staticmethod
    def get(request):
        form = CreateUserForm
        data = {'form': form}
        return render(request, 'PokeMainApp/registration.html', data)

    def post(self, request):
        try:
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('main')
            else:
                return redirect('reg')

        except Exception:
            return redirect('reg')


class PokemonApi(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin):
    serializer_class = PokemonApiSerializer
    queryset = UserPokemons.objects.all()

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
