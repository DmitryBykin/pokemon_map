# Generated by Django 2.2.3 on 2019-07-24 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0002_pokemonelementtype_pokemontemp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemontemp',
            name='element_type',
            field=models.ManyToManyField(to='pokemon_entities.PokemonElementType'),
        ),
    ]