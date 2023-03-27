import datetime

korisnik = {}
korisnik['ime'] = input('\nUnesite ime korisnika: ').title()
korisnik['prezime'] = input('Unesite prezime korisnika: ').title()
korisnik['broj'] = int(input('Unesite telefon korisnika: '))
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
      prodaja['artikl']['opis'], '\n\t\tCijena:', prodaja['artikl']['cijena'], '\nDatum isteka prodaje:',
      '\n\t\tDan:', dan, '\n\t\tMjesec:', mjesec, '\n\t\tGodina:', godina, '\nInformacije o korisniku:', '\n\t   ',
      prodaja['korisnik']['ime'], prodaja['korisnik']['prezime'], '\n\t\tTelefon:',
      prodaja['korisnik']['broj'], '\n\t\tEmail:', prodaja['korisnik']['email'])
