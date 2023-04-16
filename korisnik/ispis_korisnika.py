from telefon import ispis_telefona
def ispis_korisnika(korisnik):
    print('Informacije o korisniku: ')
    print(f"\tIme: {korisnik['ime']}")
    print(f"\tPrezime: {korisnik['prezime']}")
    print(f"\tEmail: {korisnik['email']}")
    ispis_telefona(korisnik['telefon'])

def get_korisnik(redni_broj, korisnik):
    return f"{redni_broj}.  {korisnik['ime']} {korisnik['prezime']}"

def ispis_svih_korisnika(korisnici):
    for korisnik in korisnici:
        ispis_korisnika(korisnik)