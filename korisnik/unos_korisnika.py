from .Korisnik import Korisnik
from utilities import unos_telefona
from .unos_osobne import unos_osobne
def unos_korisnika(redni_broj):
    ime = input(f'Unesite ime {redni_broj}. korisnika: ').capitalize()
    prezime = input(f'Unesite prezime {redni_broj}. korisnika: ').capitalize()
    email = input(f'Unesite email {redni_broj}. korisnika: ').strip()
    telefon = unos_telefona(f'Unesite telefon {redni_broj}. korisnika: ')
    osobna = unos_osobne(redni_broj)
    return Korisnik(ime, prezime, email, telefon, osobna)







