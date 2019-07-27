from django.db import models


# your models here
class PokemonElementType(models.Model):
    title = models.CharField(max_length=200, verbose_name='стихия', null=True)

    def __str__(self):
        return self.title


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200, verbose_name='название на русском', default='')
    title_en = models.CharField(max_length=200, verbose_name='название на английском', blank=True, default='')
    title_jp = models.CharField(max_length=200, verbose_name='название на японском', blank=True, default='')

    image = models.ImageField(upload_to='images', blank=True, null=True, verbose_name='изображение')

    description = models.TextField(blank=True, verbose_name='описание', default='')

    next_evolution = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True,
                                       related_name='+', verbose_name='в кого эволюционирует')
    previous_evolution = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True,
                                           related_name='+', verbose_name='из кого эволюционировал')
    element_type = models.ManyToManyField(PokemonElementType)

    def __str__(self):
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='покемон')

    lat = models.FloatField(blank=True, verbose_name='широта', default=0)
    lon = models.FloatField(blank=True, verbose_name='долгота', default=0)

    appeared_at = models.DateTimeField(blank=True, null=True, verbose_name='появился')
    disappeared_at = models.DateTimeField(blank=True, null=True, verbose_name='исчез')

    level = models.IntegerField(blank=True, verbose_name='уровень', default=0)
    health = models.IntegerField(blank=True, verbose_name='здоровье', default=0)
    strength = models.IntegerField(blank=True, verbose_name='сила', default=0)
    defence = models.IntegerField(blank=True, verbose_name='атака', default=0)
    stamina = models.IntegerField(blank=True, verbose_name='выносливость', default=0)

