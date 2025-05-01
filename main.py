def begruessung(name):
    print(f"Hallo, {name}! Willkommen im SAP Bootcamp.")
    
def waehrungsrechner(euro_betrag):
    wechselkurs = 1.08
    usd_betrag = euro_betrag * wechselkurs
    print(f"{euro_betrag} Euro sind {usd_betrag:.2f} US-Dollar.")


    # Aktiviere nur einen dieser Blöcke:

    # Begrüßung
    # name = input("Wie heißt du? ")
    # begruessung(name)

    # Währungsumrechner

    # eingabe = input("Wie viele Euro möchtest du umrechnen? ")
    # euro = float(eingabe)
    # waehrungsrechner(euro)
      
def eur_to_usd(betrag):
        kurs = 1.08
        return betrag * kurs

def usd_to_eur(betrag):
        kurs = 1.08
        return betrag / kurs

def begruessung(name):
     print(f"Hallo, {name}! WIllkommen im SAP Bootcamp.")

def verdopple_euro(betrag):
     return betrag * 2

if __name__ == "__main__":
      
# Menü anzeigen
    while True:
        print("\n--- Willkommen beim Währungsrechner! ---")
        print("1: EUR -> UDS")
        print("2: USD -> EUR")
        print("3: Begrüßung anzeigen")
        print("4: Euro-Betrag verdoppeln")
        print("q: Beenden")

        wahl = input("Bitte Option wählen: ")

        if wahl == "1":
            eingabe = input("Betrag in EUR: ")
            euro = float(eingabe)
            usd = eur_to_usd(euro)
            print(f"{euro:.2f} EUR sind {usd:.2f} USD.")
        elif wahl == "2":
            eingabe = input("Betrag in USD: ")
            usd = float(eingabe)
            euro = usd_to_eur (usd)
            print(f"{usd:.2f} USD sind {euro:.2f} EUR. ")
        elif wahl == "3":
            name = input("Wie heißt du?")
            begruessung(name)
            
        elif wahl == "4":
            eingabe = input("Betrag in EUR: ")
            euro = float(eingabe)
            doppelter_betrag = verdopple_euro(euro)
            print(f"{euro:.2f} EUR verdoppelt sind {doppelter_betrag:.2f} EUR.")
        elif wahl.lower() == "q":
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        
        else:
            print("Ungültige Auswahl - bitte 1, 2, 3, 4 oder q eingeben.")

