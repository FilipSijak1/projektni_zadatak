import datetime

korisnik = {}
korisnik['ime'] = input('\nUnesite ime korisnika: ').title()
korisnik['prezime'] = input('Unesite prezime korisnika: ').title()
telefon = {}
telefon['pozivni_broj'] = int(input('Unesite pozivni broj: '))
telefon['broj'] = int(input('Unesite broj telefona: '))
telefon['proizvodac_mobitela'] = input('Unesite preoizvođaća mobitela: ')
korisnik['broj'] = telefon
korisnik['email'] = input('Unesite email adresu korisnika: ').strip()

artikl = {}
artikl['naslov'] = input('Unesite naslov artikla: ')
artikl['opis'] = input('Unesite opis artikla: ')
artikl['cijena'] = float(input('Unesite cijenu artikla: '))

dan = int(input('Unesite dan isteka prodaje: '))
mjesec = int(input('Unesite mjesec isteka prodaje: '))
godina = int(input('Unesite godinu isteka prodaje: '))

date = datetime.date(godina, mjesec, dan)

prodaja = {}
prodaja['datum'] = date
prodaja['korisnik'] = korisnik
prodaja['artikl'] = artikl

print('Informacije o artiklu:', '\n\t\tNaslov:', prodaja['artikl']['naslov'], '\n\t\tOpis:',
      prodaja['artikl']['opis'], '\n\t\tCijena:', prodaja['artikl']['cijena'])
print('Datum isteka prodaje:','\n\t\tDan:', prodaja['datum'].day, '\n\t\tMjesec:', prodaja['datum'].month,
      '\n\t\tGodina:', prodaja['datum'].year)
print('Informacije o korisniku:', '\n\t   ', prodaja['korisnik']['ime'], prodaja['korisnik']['prezime'],
      '\n\t\tTelefon:', '\n\t\t\tPozivni broj: ', prodaja['korisnik']['broj']['pozivni_broj'], '\n\t\t\tBroj:',
      prodaja['korisnik']['broj']['broj'], '\n\t\t\tProizvođač mobitela:',
      prodaja['korisnik']['broj']['proizvodac_mobitela'], '\n\t\tEmail:', prodaja['korisnik']['email'])

