class OsobnaIskaznica:
    def __init__(self, broj, prebivaliste, oib):
        self.__broj = broj
        self.__prebivaliste = prebivaliste
        self.__oib = oib

    @property
    def broj(self):
        return self.__broj

    @broj.setter
    def broj(self, broj):
        self.__broj = broj

    @property
    def prebivaliste(self):
        return self.__prebivaliste

    @prebivaliste.setter
    def prebivaliste(self, prebivaliste):
        self.__prebivaliste = prebivaliste

    @property
    def oib(self):
        return self.__oib

    @oib.setter
    def oib(self, oib):
        self.__oib = oib

    def ispis(self):
        print(f"Informacije o osobnoj iskaznici:")
        print(f"\tBroj osobne iskaznice: {self.__broj}")
        print(f"\tPrebivalište s osobne iskaznice: {self.__prebivaliste}")
        print(f"\tOIB s osobne iskaznice: {self.__oib}")

