from .Korisnik import Korisnik
from utilities import unos_telefona, unos_pozitivnog_cijelog_broja
from .OsobnaIskaznica import OsobnaIskaznica
def unos_korisnika(redni_broj):
    ime = input(f'Unesite ime {redni_broj}. korisnika: ').capitalize()
    prezime = input(f'Unesite prezime {redni_broj}. korisnika: ').capitalize()
    email = input(f'Unesite email {redni_broj}. korisnika: ').strip()
    telefon = unos_telefona(f'Unesite telefon {redni_broj}. korisnika: ')
    osobna = unos_osobne(redni_broj)
    return Korisnik(ime, prezime, email, telefon, osobna)

def unos_osobne(redni_broj):
    print("Unesite podatke osobne iskaznice:")
    broj = unos_pozitivnog_cijelog_broja(f"Unesite broj {redni_broj}. osobne iskaznice:")
    prebivaliste = input(f"Unesite prebivalište s {redni_broj}. osobne iskaznice: ")
    oib = unos_pozitivnog_cijelog_broja(f"Unesite OIB s {redni_broj}. osobne iskaznice: ")
    return OsobnaIskaznica(broj, prebivaliste, oib)

