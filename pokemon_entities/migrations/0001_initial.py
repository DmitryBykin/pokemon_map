# Generated by Django 2.2.3 on 2019-07-23 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_ru', models.CharField(max_length=200, null=True, verbose_name='название на русском')),
                ('title_en', models.CharField(blank=True, max_length=200, null=True, verbose_name='название на английском')),
                ('title_jp', models.CharField(blank=True, max_length=200, null=True, verbose_name='название на японском')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='изображение')),
                ('description', models.TextField(blank=True, null=True, verbose_name='описание')),
                ('next_evolution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='pokemon_entities.Pokemon', verbose_name='в кого эволюционирует')),
                ('previous_evolution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='pokemon_entities.Pokemon', verbose_name='из кого эволюционировал')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(blank=True, null=True, verbose_name='широта')),
                ('lon', models.FloatField(blank=True, null=True, verbose_name='долгота')),
                ('appeared_at', models.DateTimeField(blank=True, null=True, verbose_name='появился')),
                ('disappeared_at', models.DateTimeField(blank=True, null=True, verbose_name='исчез')),
                ('level', models.IntegerField(blank=True, null=True, verbose_name='уровень')),
                ('health', models.IntegerField(blank=True, null=True, verbose_name='здоровье')),
                ('strength', models.IntegerField(blank=True, null=True, verbose_name='сила')),
                ('defence', models.IntegerField(blank=True, null=True, verbose_name='атака')),
                ('stamina', models.IntegerField(blank=True, null=True, verbose_name='выносливость')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pokemon_entities.Pokemon', verbose_name='покемон')),
            ],
        ),
    ]