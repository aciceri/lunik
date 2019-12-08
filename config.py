from datetime import date
from os import environ
from yaml import safe_load

assets_path = 'assets'
generated_path = '_dist'
images_path = 'images'
films_path = 'films.yaml'
img_width = 1000

with open(films_path, 'r') as f:
    films = safe_load(f)

movies = [{'title': key, **films[key]} for key in films]

values = {'gmaps_place_id': 'ChIJ3b1qkdK3hkcRe7llxcKzCvM',
          'gmaps_key': environ['GMAPS_KEY'],
          'movies': movies,
          'footer': f'Associazione culturale Lunik — Ultimo aggiornamento del {date.today().strftime("%d/%m/%Y")}'}
