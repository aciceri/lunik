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
facebook_page = 'http://fb.me/cineforumlunik'
intro = cleandoc("""
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce a est sollicitudin, dictum mauris
efficitur, luctus ex. Fusce iaculis, mi quis iaculis cursus, nibh arcu rutrum tortor, eget facilisis
mauris nisi eget tellus. Morbi tincidunt arcu eu sollicitudin dapibus. Aliquam sagittis risus quis
neque suscipit auctor. Maecenas eu justo pharetra elit malesuada convallis sit amet vitae
nunc. Nullam ipsum lorem, venenatis sed quam quis, luctus lacinia ipsum.
""")
contacts = cleandoc(f"""
Per qualsiasi informazione aggiuntiva puoi contattarci tramite la <a href='{facebook_page}'>nostra
pagina Facebook</a> o direttamente alla nostra e-mail <a href='mailto:{email}'>{email}</a>.
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
