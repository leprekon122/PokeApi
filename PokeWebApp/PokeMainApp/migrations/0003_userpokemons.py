# Generated by Django 4.0.5 on 2022-06-13 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PokeMainApp', '0002_alter_pokemoninfo_detail_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPokemons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=255)),
                ('pokemon_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PokeMainApp.pokemoninfo')),
            ],
            options={
                'verbose_name': 'UserPokemons',
                'verbose_name_plural': 'UserPokemons',
            },
        ),
    ]
