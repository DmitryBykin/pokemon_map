# Generated by Django 2.2.3 on 2019-07-30 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0009_auto_20190730_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='element_type',
            field=models.ManyToManyField(blank=True, to='pokemon_entities.PokemonElementType'),
        ),
    ]