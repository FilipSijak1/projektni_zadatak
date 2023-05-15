from artikl import unos_artikla
from utilities import unos_pozitivnog_cijelog_broja
from .Kategorija import Kategorija
def unos_kategorije(redni_broj):
    naziv = input(f'Unesite naziv {redni_broj}. kategorije: ')

    artikli = []
    br_artikala = (unos_pozitivnog_cijelog_broja(f'Unesite broj artikala za {redni_broj}. kategoriju: '))
    for i in range(1, br_artikala + 1):
        artikli.append(unos_artikla(i))

    return Kategorija(naziv, artikli)