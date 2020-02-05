from datetime import date
from os import environ
from inspect import cleandoc
from yaml import safe_load

assets_path = 'assets'
generated_path = '_dist'
images_path = 'images'
films_path = 'films.yaml'
img_width = 1000
email = 'contatti@lunik.it'
facebook_page = 'https://fb.me/cineforumlunik'
instagram_page = 'https://www.instagram.com/cineforumlunik'
intro = cleandoc("""
Rinasce Lunik. Da Febbraio 2020 ritorna il cineforum storico di Cernusco, il quale si prefigge una entusiasmante
stagione cinematografica riproponendo film d'autore e non, con l'obiettivo di far riscoprire della discussione.
L'associazione culturale Lunik non è solo cinema, ma anche serie tv, fumetti, videogiochi e tanto altro.
Il sogno di una generazione di ragazze e ragazzi ritorna.
""")
contacts = cleandoc(f"""
Per qualsiasi informazione aggiuntiva puoi contattarci tramite la <a href='{facebook_page}'>nostra
pagina Facebook</a>, <a href='{instagram_page}'>Instagram</a> o
direttamente alla nostra e-mail <a href='mailto:{email}'>{email}</a>.
<br>
Le proiezioni hanno luogo presso la sede della <a href='https://www.edifcernusco.it/'>Cooperativa
Edificatrice Cernuschese</a>, ti aspettiamo!
""")
footer = cleandoc(f"""
Associazione culturale Lunik — Ultimo aggiornamento del {date.today().strftime("%d/%m/%Y")}
""")

with open(films_path, 'r') as f:
    films = safe_load(f)

movies = [{'title': key, **films[key]} for key in films]

values = {'gmaps_place_id': 'ChIJ3b1qkdK3hkcRe7llxcKzCvM',
          'gmaps_key': environ['GMAPS_KEY'],
          'intro': intro,
          'movies': movies,
          'contacts': contacts,
          'footer': footer}
