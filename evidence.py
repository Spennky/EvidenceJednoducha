from pojistenec import Pojistenec


class Evidence:
    def __init__(self):
        self.pojistenci = []

    # Volba 1
    def pridat_pojisteneho(self, novy_pojistenec):
        self.pojistenci.append(novy_pojistenec)
        input("\nData byla uložena, pokračujte stiskem klávesy ENTER...")

    # Volba 2
    def vypsat_pojistene(self):
        for pojistenec in self.pojistenci:
            print(pojistenec)
        input("\nPokračujte stiskem klávesy ENTER...")

    # Volba 3
    def vyhledat_pojistneho(self):
        jmeno = input("Zadejte jméno: ").lower()
        prijmeni = input("Zadejte příjmení: ").lower()
        pojistenec_nalezen = 1
        for pojistenec in self.pojistenci:
            if pojistenec.prijmeni.lower() == prijmeni and pojistenec.jmeno.lower() == jmeno:
                pojistenec_nalezen = 0
                print(pojistenec)
        if pojistenec_nalezen == 1:
            print("Žádný pojištěný s tímto příjmením nebyl nalezen.")
        input("\nPokračujte Pokračujte stiskem klávesy ENTER...")

    def vyber(self):
        while True:
            print()
            volba = input("Vyberte operaci:\n[1]Přidat nového pojištěného\n[2]Výpis všech pojištěných"
                          "\n[3]Vyhledat pojištěného\n[4]Konec\n")

            if volba == '1':
                while True:
                    jmeno = input("Zadejte jméno: ")
                    if len(jmeno) >= 2:
                        break
                    else:
                        print("Jméno musí mít alespoň 2 znaky!")
                while True:
                    prijmeni = input("Zadejte příjmení: ")
                    if len(prijmeni) >= 2:
                        break
                    else:
                        print("Příjmení musí mít alespoň 2 znaky!")
                while True:
                    vek = input("Zadejte věk: ")
                    if vek.isdigit():
                        break
                    else:
                        print("Vyžadováno číselné zadání. Zkuste znovu.")
                while True:
                    telefon = input("Zadejte telefonní číslo: ")
                    if telefon.isdigit():
                        break
                    else:
                        print("Vyžadováno číselné zadání. Zkuste znovu.")
                novy_pojistenec = Pojistenec(jmeno, prijmeni, vek, telefon)
                self.pridat_pojisteneho(novy_pojistenec)

            elif volba == '2':
                self.vypsat_pojistene()

            elif volba == '3':
                self.vyhledat_pojistneho()

            elif volba == '4':
                break

            else:
                print("Neplatná volba")
