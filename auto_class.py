# Aufgabe 2: Erstellen einer Klasse Auto, mit der Unterklasse Kombi.

class Auto:
    """
    Erstellt das Objekt Auto für einen Gebrauchtwagenhändler
    """
    anzahl = 0

    def __init__(self, ma, mo, bj, pr):
        """
        Initialisiert ein neues Objekt Auto
        Argumente:
        * Marke(String): Marke des Gebrauchtwagen
        * Modell(String): Modell des Gebrauchtwagens
        * Baujahr(int): Baujahr des Fahrzeugs
        * Preis(int): Angestrebter Verkaufspreis
        """
        self.__Marke = ma
        self.__Modell = mo
        self.__Baujahr = bj
        self.__Preis = pr
        Auto.anzahl += 1
    def __del__(self):
        """
        Löscht das Objekt Auto
        """
        Auto.anzahl -= 1
    
    def getMarke(self):
        """
        Gibt die Marke des Autos zurück
        """
        return self.__Marke
    def getModell(self):
        """
        Gibt das Modell des Autos zurück
        """
        return self.__Modell
    def getBaujahr(self):
        """
        Gibt das Baujahr des Autos zurück
        """
        return self.__Baujahr
    def getPreis(self):
        """
        Gibt den Verkaufspreis des Autos zurück
        """
        return self.__Preis
    def setPreis(self, preis_neu):
        """
        Ändert den Preis des Autos
        """
        if abs(self.__Preis - preis_neu) < self.__Preis * 0.05:
            self.__Preis = preis_neu
        else:
            print("Die Abweichung vom vorherigen Preis ist sehr groß.")
            bestaetigung = input("Soll %d als neuer Preis"%preis_neu + "festgelegt werden (ja/nein)")
            if bestaetigung == "ja":
                self.__Preis = preis_neu
class Kombi(Auto):
    """
    Erstellt das Objekt Kombi, abgeleitet von der Klasse Auto
    """
    def __init__(self, ma, mo, bj, pr, vol):
        """
        Initialisiert ein neues Objekt Kombi
        Argumente:
        * Marke(String): Marke des Gebrauchtwagen
        * Modell(String): Modell des Gebrauchtwagens
        * Baujahr(int): Baujahr des Fahrzeugs
        * Preis(int): Angestrebter Verkaufspreis
        * Volumen(int): Volumen des Kofferraums
        """
        Auto.__init__(self, ma, mo, bj, pr)
        self.__Volumen = vol

    def getVolumen(self):
        """
        Gibt das Kofferraumvolumen zurück
        """
        return self.__Volumen
kombi1 = Kombi("Renault", "Laguna", 2012, 6000, 508)
print(kombi1.getMarke(), kombi1.getModell(), kombi1.getBaujahr(), kombi1.getPreis(), kombi1.getVolumen())

