from django.db import models


# Create your models here.

class PokemonInfo(models.Model):
    name = models.CharField(max_length=255)
    detail_url = models.TextField()

    def __str__(self):
        return f"{self.name} {self.detail_url}"

    class Meta:
        verbose_name = 'PokemonInfo'
        verbose_name_plural = "Pokemon's Info"


class UserPokemons(models.Model):
    user_name = models.CharField(max_length=255)
    pokemon_name = models.ForeignKey(PokemonInfo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user_name} {self.pokemon_name}"

    class Meta:
        verbose_name = 'UserPokemons'
        verbose_name_plural = 'UserPokemons'
