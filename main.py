
from CrudPojisteneho import CrudPojisteneho
from Pojisteni import Pojisteni
import sqlite3

def fetch_data(query, c, parametr=None):
    if parametr:
        c.execute(query, parametr)
    else:
        c.execute(query)
    data = c.fetchall()
    return data

conn = sqlite3.connect('Evidence pojisteni.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS PojistenaOsoba (jmeno TEXT, prijmeni TEXT, datum_narozeni TEXT, tel_cislo TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS Pojisteni (typ TEXT, cena INTEGER, cislo_pojisteni TEXT, jmeno TEXT, prijmeni TEXT, FOREIGN KEY (jmeno, prijmeni) REFERENCES PojistenaOsoba(jmeno, prijmeni))")

def main():
    spustit = CrudPojisteneho()
    spustit_pojisteni = Pojisteni()

    while True:
        print("1. Přidat pojištěného")
        print("2. Zobrazit seznam pojištěných")
        print("3. Najít pojištěného")
        print("4. Přidat pojistku")
        print("5. Zobrazit detaily pojištěného")
        print("6. Zobrazit detaily pojistky")
        print("7. Smazat pojištěného a jeho pojištění")
        print("8. Upravit pojištěného")
        print("9. Upravit pojistku")
        print("10. Konec")

        choice = input("Zadejte svou volbu: ")

        if choice == "1":
            spustit.pridat_pojisteneho(c, conn)

        elif choice == "2":
            spustit.seznam_pojistenych(c, fetch_data)

        elif choice == "3":
            spustit.najit_pojisteneho(fetch_data, c)

        elif choice == "4":
            spustit_pojisteni.pridat_pojisteni(fetch_data, c, conn)

        elif choice == "5":
            spustit.detaily_pojisteny(fetch_data, c)

        elif choice == "6":
            spustit_pojisteni.detaily_pojistek(fetch_data, c)

        elif choice == "7":
            spustit_pojisteni.smazat(conn, c)

        elif choice == "8":
            spustit.edit_pojisteneho(fetch_data, c, conn)

        elif choice == "9":
            spustit_pojisteni.edit_pojisteni(fetch_data, c, conn)

        elif choice == '10':
            conn.close()
            break

if __name__ == "__main__":
    main()

