from datetime import date


assets_path = 'assets'
generated_path = '_dist'
images_path = 'images'

movies = [{
    'title': 'Kill Bill',
    'when': '11 Gennaio 2019 alle 21:00',
    'image': 'killbill.jpg',
    'desc': '''
É possibile creare un’opera che coniughi in un cocktail di generi la febbrile passione per la
settima arte? Per Quentin Tarantino non c’é niente di più naturale e stimolante. Ideato come regalo
per il trentesimo compleanno di Uma Thurman, Kill Bill rimane ancora oggi una delle principali opere
del regista statunitense, il suo canto del cigno e la sua più grande dichiarazione d’amore per il
cinema.
'''
    }, {
    'title': 'El Topo',
    'when': '23 Gennaio 2019 alle 21:00',
    'image': 'eltopo.jpg',
    'desc': '''
I film più surrealisti e visionari raramente riescono a diventare grandi successi di pubblico, ma
molti di questi nel tempo arrivano a diventar dei veri e propri cult movie, ed è proprio questo il
caso di El Topo (1970) di Alejandro Jodorowski.
'''    
    }, {
    'title': 'La corazzata Potemkin',
    'when': '15 Febbraio 2019 alle 21:00',
    'image': 'potemkin.jpg',
    'desc': '''
Si tratta di una delle più note e influenti opere della storia del cinema, e per i suoi valori
tecnici ed estetici è generalmente ritenuto fra i migliori film del '900 nonché una delle più
compiute espressioni cinematografiche. Prodotto dal primo stabilimento del Goskino a Mosca, fu
presentato il 21 dicembre 1925 al teatro Bol'šoj. La prima proiezione aperta al pubblico avvenne il
21 gennaio 1926.'''
    }, {
    'title': 'Stalker',
    'when': '28 Febbraio 2019 alle 21:00',
    'image': 'stalker.jpg',
    'desc':  '''
Film di fantascienza del 1979 diretto da Andrej Tarkovskij, liberamente tratto dal romanzo Picnic
sul ciglio della strada (1971) dei fratelli Arkadij e Boris Strugackij.  Come già per Solaris, la
pellicola rappresenta una personale interpretazione di Tarkovskij dello scritto originale.  Pur
essendo la trama ascrivibile al genere fantascientifico, la sua struttura narrativa, così come le
tematiche affrontate, appartengono al cinema d'autore. Il lento e profondo viaggio catartico
compiuto all'interno della cosiddetta "Zona", dove le tre diverse concezioni della vita dei
protagonisti si scontrano e si mettono in discussione, trascende i dettami del film di genere.
'''
}]

values = {'gmaps_place_id': 'ChIJ3b1qkdK3hkcRe7llxcKzCvM',
          'gmaps_key': '',
          'movies': movies,
          'footer': f'Associazione culturale Lunik — Ultimo aggiornamento del {date.today().strftime("%d/%m/%Y")}'}
