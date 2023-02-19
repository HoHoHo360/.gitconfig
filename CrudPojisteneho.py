
class CrudPojisteneho:
    def __init__(self):
        self.pojisteni_lide = []

    def pridat_pojisteneho(self, c, conn):
        jmeno = input("Křestní jméno: ")
        prijmeni = input("Přijmení: ")
        datum_narozeni = input("Datum narození: ")
        tel_cislo = input("Tel. číslo: ")
        c.execute("INSERT INTO PojistenaOsoba (jmeno, "
                  "prijmeni, "
                  "datum_narozeni, "
                  "tel_cislo) VALUES (?, ?, ?, ?)",
                  (jmeno, prijmeni, datum_narozeni, tel_cislo))
        conn.commit()
        print("Pojištěný je přidán do seznamu")

    def seznam_pojistenych(self, c, fetch_data):
        query = "SELECT * FROM PojistenaOsoba"
        data = fetch_data(query, c)
        for osoba in data:
            print(f"Jméno: {osoba[0]} {osoba[1]}, "
                  f"Datum narození: {osoba[2]}, "
                  f"Tel. číslo: {osoba[3]}")

    def najit_pojisteneho(self, fetch_data, c):
        jmeno = input("Křestní jméno: ")
        prijmeni = input("Přijmení: ")
        query = "SELECT * FROM PojistenaOsoba WHERE jmeno=? AND prijmeni=?"
        data = fetch_data(query, c, (jmeno, prijmeni))
        if data:
            for osoba in data:
                print(f"Jméno: {osoba[0]} {osoba[1]}, "
                      f"Datum narození: {osoba[2]}, "
                      f"Tel. číslo: {osoba[3]}")
        else:
            print("Pojištěný nebyl nalezen")

    def edit_pojisteneho(self, fetch_data,c, conn):
        jmeno = input("Křestní jméno: ")
        prijmeni = input("Přijmení: ")
        query = "SELECT * FROM PojistenaOsoba WHERE jmeno=? AND prijmeni=?"
        data = fetch_data(query, c, (jmeno, prijmeni))
        if data:
            for osoba in data:
                nove_jmeno = input("Nové křestní jméno: ")
                nove_prijmeni = input("Nové přijmení: ")
                novy_vek = input("Nové datum narození: ")
                nove_tel_cislo = input("Nové tel. číslo: ")
                c.execute(
                    "UPDATE PojistenaOsoba SET jmeno=?, "
                    "prijmeni=?, "
                    "datum_narozeni=?, "
                    "tel_cislo=? WHERE jmeno=? AND prijmeni=?",
                    (nove_jmeno, nove_prijmeni, novy_vek,
                     nove_tel_cislo, jmeno, prijmeni))
                conn.commit()
                c.execute(
                    "UPDATE Pojisteni SET jmeno=?, "
                    "prijmeni=? WHERE jmeno=? AND prijmeni=?",
                    (nove_jmeno, nove_prijmeni, jmeno, prijmeni))
                conn.commit()
                print("Pojištěný byl upraven")
        else:
            print("Pojištěný nebyl nalezen")

    def detaily_pojisteny(self, fetch_data, c):
        jmeno = input("Křestní jméno: ")
        prijmeni = input("Přijmení: ")
        query = "SELECT * FROM PojistenaOsoba WHERE jmeno=? AND prijmeni=?"
        data = fetch_data(query, c, (jmeno, prijmeni))
        if data:
            for osoba in data:
                print(f"Jméno: {osoba[0]} {osoba[1]}, "
                      f"Datum narození: {osoba[2]}, "
                      f"Tel. číslo: {osoba[3]}")
            query = "SELECT * FROM Pojisteni WHERE jmeno=? AND prijmeni=?"
            data = fetch_data(query, c, (jmeno, prijmeni))
            if data:
                print("Pojištení:")
                for pojisteni in data:
                    print(f"Předmět pojištění: {pojisteni[0]}, "
                          f"Cena: {pojisteni[1]} Kč, "
                          f"Číslo pojištění: {pojisteni[2]}, ")
        else:
            print("Pojištěný nebyl nalezen")



