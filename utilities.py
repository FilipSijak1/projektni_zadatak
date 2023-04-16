from datetime import date
def unos_pozitivnog_cijelog_broja(poruka_cijeli_broj):
    while True:
        try:
            value = int(input(poruka_cijeli_broj))
            if value <= 0:
                raise Exception('Niste unijeli pozitivan cijeli broj. Ponovno unesite pozitivan cijeli broj!')

        except ValueError:
            print('Unijeli ste znak umjesto cijelg broja. Ponovno unesite pozitivan cijeli broj!')
        except Exception as e:
            print(e)
        else:
            return value

def unos_datuma(poruka_datum):
    while True:
        try:
            print('Unos datuma završetka prodaje:')
            dan = int(input(poruka_datum))
            mjesec = int(input(f'\t\tUnesite mjesec isteka prodaje: '))
            godina = int(input(f'\t\tUnesite godinu isteka prodaje: '))
            datum = date(godina, mjesec, dan)

        except ValueError as e:
            print(e)
        else:
            return datum

def unos_intervala(min, max):
    while True:
        try:
            broj = int(input('Odaberite akciju: '))

            if broj < min or broj > max:
                raise Exception('Unijeli ste broj koji nije u intervalu.')

        except ValueError:
            print('Unijeli ste slovo umjesto broja.')

        except Exception as e:
            print(e)

        else:
            return broj

