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
     
     while True:
        print(f"Willkommen bei deiner SAP-Bewerbungshilfe!")
        print("1:Was ist SAP BTP?")
        print("2:Was macht ein Software Engineer?")
        print("3:Was sind deine Stärken?")
        print("4:Beenden")

        wahl = input("Bitte Option wählen:")
        
        if wahl == "1":
             eingabe = input("Was ist SAP BTP?")
             print("Die SAP Business Technology Platform (BTP) ist eine Cloud-Plattform für Daten, Integration, KI und Anwendungsentwicklung.")
        elif wahl == "2":
             eingabe = input("Was macht ein Software Engineer?")
             print("Er entwickelt Software, höhöhö!")
        elif wahl == "3":
            eingabe = input("Was sind deine Stärken?")
            print("Gaming, Fußball und Leute nerven")
        elif wahl == "4":
            print("Programm wird beendet.")
            break

        else:
             print("Ungültige Auswahl!")

