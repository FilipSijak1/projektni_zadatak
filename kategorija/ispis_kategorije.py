from .Kategorija import Kategorija

def get_kategorija(redni_broj, kategorija):
    return f"{redni_broj}.  {kategorija.naziv}"

def ispis_svih_kategorija(kategorije):
    for kategorija in kategorije:
        print(f"{Kategorija.naziv}:")
        for artikl in kategorija.artikli:
            artikl.ispis()
