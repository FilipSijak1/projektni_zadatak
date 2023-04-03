from datetime import date

korisnici = []
kategorije = []
prodaje = []

broj_korisnika = int(input('Unesite broj korisnika: '))
for i in range(1, broj_korisnika+1):
    korisnik = {}
    korisnik['ime'] = input(f'Unesite ime {i}. korisnika: ').capitalize()
    korisnik['prezime'] = input(f'Unesite prezime {i}. korisnika: ').capitalize()
    korisnik['telefon'] = int(input(f'Unesite telefon {i}. korisnika: '))
    korisnik['email'] = input(f'Unesite email {i}. korisnika: ').strip()
    korisnici.append(korisnik)

broj_kategorija = int(input('Unesite broj kategorija: '))
for i in range(1, broj_kategorija+1):
    kategorija = {}
    kategorija['naziv'] = input(f'Unesite naziv {i}. kategorije: ')
    kategorija['artikli'] = []

    broj_artikala = int(input(f'Unesite broj artikala za {i}. kategoriju: '))
    for j in range(1, broj_artikala+1):
        artikl = {}
        artikl['naslov'] = input(f'Unesite naslov {j}. artikla: ')
        artikl['opis'] = input(f'Unesite opis {j}. artikla: ')
        artikl['cijena'] = float(input(f'Unesite cijenu {j}. artikla: '))
        kategorija['artikli'].append(artikl)

    kategorije.append(kategorija)

broj_prodaja = int(input('Unesite broj prodaja: '))
for i in range(1, broj_prodaja+1):
    prodaja = {}
    dan = int(input(f'Unesite dan isteka {i}. prodaje: '))
    mjesec = int(input(f'Unesite mjesec isteka {i}. prodaje: '))
    godina= int(input(f'Unesite godinu {i}. prodaje: '))
    prodaja['datum'] = date(godina, mjesec, dan)

    #odabir korisnika
    print(f'Odaberite korisnika {i}. prodaje: ')
    for j, korisnik in enumerate(korisnici, start=1):
        print(f'\t{j}. {korisnik["ime"]} {korisnik["prezime"]}')
    odabir_korisnika = int(input('Odabrani korisnik: '))

    #odabir kategorije
    print(f'Odaberite kategoriju {i}. prodaje: ')
    for j, kategorija in enumerate(kategorije, start=1):
        print(f'\t{j}. {kategorija["naziv"]}')
    odabir_kategorije = int(input('Odabrana kategorija: '))

    #odabir artikla
    print(f'Odaberite artikl {i}. prodaje: ')
    for j, artikl in enumerate(kategorije[odabir_kategorije-1]['artikli'], start=1):
        print(f'\t{j}. {kategorije[odabir_kategorije-1]["artikli"][j-1]["naslov"]}')
    odabir_artikla = int(input('Odabrani artikl: '))

    prodaja['korisnik'] = korisnici[odabir_korisnika-1]
    prodaja['artikl'] = kategorije[odabir_kategorije-1]['artikli'][odabir_artikla-1]
    prodaje.append(prodaja)

for i, prodaja in enumerate(prodaje, start=1):
    print(f'Prodaja {i}.: ')
    print('Informacije o korisniku: ')
    print(f'\tIme: {prodaja["korisnik"]["ime"]}')
    print(f'\tIme: {prodaja["korisnik"]["prezime"]}')
    print(f'\tTelefon: {prodaja["korisnik"]["telefon"]}')
    print(f'\tEmail: {prodaja["korisnik"]["email"]}')

    print('Informacije o artiklu: ')
    print(f'\tnaslov: {prodaja["artikl"]["naslov"]}')
    print(f'\topis: {prodaja["artikl"]["opis"]}')
    print(f'\tcijena: {prodaja["artikl"]["cijena"]}')

    print('Datum isteka prodaje: ')
    print(f'\tDan: {prodaja["datum"].day}')
    print(f'\tMjesec: {prodaja["datum"].month}')
    print(f'\tGodina: {prodaja["datum"].year}')

    print('-' * 30)










