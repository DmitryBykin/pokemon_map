from django.db import models


# your models here
class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name='название на русском', null=True)
    title_en = models.CharField(max_length=200, verbose_name='название на английском', blank=True, null=True,)
    title_jp = models.CharField(max_length=200, verbose_name='название на японском', blank=True, null=True,)

    image = models.ImageField(upload_to='images', blank=True, null=True, verbose_name='изображение')

    description = models.TextField(blank=True, null=True, verbose_name='описание')

    next_evolution = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True,
                                       null=True, related_name='+',
                                       verbose_name='в кого эволюционирует')
    previous_evolution = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True,
                                           null=True, related_name='+',
                                           verbose_name='из кого эволюционировал')

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='покемон')

    lat = models.FloatField(blank=True, null=True, verbose_name='широта')
    lon = models.FloatField(blank=True, null=True, verbose_name='долгота')

    appeared_at = models.DateTimeField(blank=True, null=True, verbose_name='появился')
    disappeared_at = models.DateTimeField(blank=True, null=True, verbose_name='исчез')

    level = models.IntegerField(blank=True, null=True, verbose_name='уровень')
    health = models.IntegerField(blank=True, null=True, verbose_name='здоровье')
    strength = models.IntegerField(blank=True, null=True, verbose_name='сила')
    defence = models.IntegerField(blank=True, null=True, verbose_name='атака')
    stamina = models.IntegerField(blank=True, null=True, verbose_name='выносливость')
