class Pojistenec:
    def __init__(self, jmeno, prijmeni, vek, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def __str__(self):
        return f"Jméno: {self.jmeno: <15}\tPříjmení: {self.prijmeni: <15}\tVěk: {self.vek: <15}\tTelefon: " \
               f"{self.telefon: <15}"
