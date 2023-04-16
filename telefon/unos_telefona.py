from utilities import unos_pozitivnog_cijelog_broja
def unos_telefona(telefon_korisnika):
    telefon = {}
    telefon["broj"] = (unos_pozitivnog_cijelog_broja(f'Unesite broj telefona: '))
    telefon["pozivni_broj"] = (unos_pozitivnog_cijelog_broja(f'Unesite pozivni broj telefona: '))
    telefon["proizvodac"] = (input(f'Unesite proizvođača telefona: '))
    return telefon
