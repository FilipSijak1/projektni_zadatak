from kategorija import unos_kategorije
from korisnik import unos_korisnika
from prodaja import unos_prodaje, ispis_prodaje

korisnici = []
kategorije = []
prodaje = []

br_korisnika = int(input('Unesite broj korisnika: '))
for i in range(1,br_korisnika+1):
    korisnik = unos_korisnika(i)
    korisnici.append(korisnik)

br_kategorija = int(input('Unesite broj kategorija: '))
for i in range(1,br_kategorija+1):
    kategorija = unos_kategorije(i)
    kategorije.append(kategorija)

br_prodaja = int(input('Unesite broj prodaja: '))
for i in range(1,br_prodaja+1):
    prodaja = unos_prodaje(korisnici, kategorije, i)
    prodaje.append(prodaja)

for i,prodaja in enumerate(prodaje, start=1):
    print(f"Prodaja {i}")
    ispis_prodaje(prodaja)
