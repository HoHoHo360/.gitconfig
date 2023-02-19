
class Pojisteni:

    def detaily_pojistek(self, fetch_data, c):
        cislo_pojisteni = input("Číslo pojistky: ")
        query = "SELECT * FROM Pojisteni WHERE cislo_pojisteni=?"
        data = fetch_data(query, c, (cislo_pojisteni,))
        if data:
            for pojisteni in data:
                print(f"Předmět pojištění: {pojisteni[0]}, "
                      f"Cena: {pojisteni[1]} Kč, "
                      f"Číslo pojištění: {pojisteni[2]}, "
                      f"Jméno: {pojisteni[3]} {pojisteni[4]}")
        else:
            print("Pojistka nenalezena")

    def smazat(self, conn, c):
        jmeno = input("Křestní jméno: ")
        prijmeni = input("Přijmení: ")
        query1 = "DELETE FROM PojistenaOsoba WHERE jmeno=? AND prijmeni=?"
        result1 = c.execute(query1, (jmeno, prijmeni))
        query2 = "DELETE FROM Pojisteni WHERE jmeno=? AND prijmeni=?"
        result2 = c.execute(query2, (jmeno, prijmeni))
        if result1 and result2:
            print("Smazání bylo úspěšné.")
        else:
            print("Smazání se nezdařilo.")
        conn.commit()


    def edit_pojisteni(self, fetch_data,c, conn):
        cislo_pojisteni = input("Číslo pojistky: ")
        query = "SELECT * FROM Pojisteni WHERE cislo_pojisteni=?"
        data = fetch_data(query, c, (cislo_pojisteni,))
        if data:
            typ = input("Nový předmět pojištění: ")
            cena = input("Nová cena pojištění: ")
            query = "UPDATE Pojisteni SET typ=?, " \
                    "cena=? WHERE cislo_pojisteni=?"
            c.execute(query, (typ, cena, cislo_pojisteni))
            conn.commit()
            print("Pojištění upraveno")
        else:
            print("Pojištění nebylo nalezeno")

    def pridat_pojisteni(self, fetch_data, c, conn):
        jmeno = input("Křestní jméno: ")
        prijmeni = input("Přijmení: ")
        query = "SELECT * FROM PojistenaOsoba WHERE jmeno=? AND prijmeni=?"
        data = fetch_data(query, c, (jmeno, prijmeni))
        if data:
            for osoba in data:
                typ = input("Předmět pojištění: ")
                cena = input("Cena pojištění: ")
                cislo_pojisteni = input("Číslo pojistky: ")
                c.execute(
                    "INSERT INTO Pojisteni (typ, "
                    "cena, "
                    "cislo_pojisteni, "
                    "jmeno, "
                    "prijmeni) VALUES (?, ?, ?, ?, ?)",
                    (typ, cena, cislo_pojisteni, jmeno, prijmeni))
                conn.commit()
                print("Pojistka byla přidána")
        else:
            print("Pojištěný nebyl nalezen")

