# Erstellung der Klasse Ferienwohnung

class Wohnung:
    """
    Erfasst eine Ferienwohnung im Objekt Wohnung
    """
    def __init__(self, name, ort, betten, preis):
        """
        Initialisierung des Objektes Wohnung.
        Argumente:
        * Name(string): Name der Ferienwohunung
        * Ort(string): Standort der Ferienwohnung
        * Betten(int): Anzahl der Betten in der Ferienwohnung
        * Preis(int): Preis pro Übernachtung
        """
        self.__Name = name
        self.__Ort = ort
        self.__Betten = betten
        self.__Preis = preis
    def getName(self):
        """
        Gibt den Namen der Ferienwohnung zurück
        """
        return self.__Name
    def getOrt(self):
        """
        Gibt den Standort der Ferienwohnung zurück
        """
        return self.__Ort
    def getBetten(self):
        """
        Gibt die Anzahl der Betten in der Ferienwohnung zurück
        """
        return self.__Betten
    def getPreis(self):
        """
        Gibt den Preis der Ferienwohnung pro Übernachtung zurück
        """
        return self.__Preis
    def setPreis(self, preis):
        """
        Legt einen neuen Preis pro Übernachtung fest
        """
        self.__Preis = preis

wohnung1 = Wohnung("Meerblick", "Sylt",4,69)
wohnung2 = Wohnung("Alpen-Panorama", "Füssen",5,74)
wohnung3 = Wohnung("Am Seeufer", "Konstanz",3,58)

print("Wohnung1: ", wohnung1.getName(), wohnung1.getOrt(), wohnung1.getBetten(), wohnung1.getPreis())
print("Wohnung2: ", wohnung2.getName(), wohnung2.getOrt(), wohnung2.getBetten(), wohnung2.getPreis())
print("Wohnung3: ", wohnung3.getName(), wohnung3.getOrt(), wohnung3.getBetten(), wohnung3.getPreis())


    