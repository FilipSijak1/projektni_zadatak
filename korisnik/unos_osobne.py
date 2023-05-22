from utilities import unos_pozitivnog_cijelog_broja
from .OsobnaIskaznica import OsobnaIskaznica

def unos_osobne(redni_broj):
    print("Unesite podatke osobne iskaznice:")
    broj = unos_pozitivnog_cijelog_broja(f"\t\tUnesite broj {redni_broj}. osobne iskaznice: ")
    prebivaliste = input(f"\t\tUnesite prebivalište s {redni_broj}. osobne iskaznice: ").capitalize()
    oib = unos_pozitivnog_cijelog_broja(f"\t\tUnesite OIB s {redni_broj}. osobne iskaznice: ")
    return OsobnaIskaznica(broj, prebivaliste, oib)