from random import shuffle
from matplotlib import pyplot as plt

kolonien = True

max_zug = 100


class Geldkarte:
    def __init__(self, name, anzahl, preis, geld):
        self.name = name
        self.anzahl = anzahl
        self.preis = preis
        self.geld = geld


kupfer = Geldkarte("Kupfer", 80, 0, 1)
silber = Geldkarte("Silber", 60, 3, 2)
gold = Geldkarte("Gold", 60, 6, 3)
platin = Geldkarte("Platin", 12, 9, 5)

geldkarten = [kupfer, silber, gold]
if kolonien:
    geldkarten = geldkarten + [platin]


# max_geldwert = max(karte.preis for karte in geldkarten)


class Punktekarte:
    def __init__(self, name, anzahl, preis, punkte):
        self.name = name
        self.anzahl = anzahl
        self.preis = preis
        self.punkte = punkte


anzahl_punktekarten = 12
fluch = Punktekarte("Fluch", 40, 0, -1)
anwesen = Punktekarte("Anwesen", anzahl_punktekarten, 2, 1)
herzogtum = Punktekarte("Herzogtum", anzahl_punktekarten, 5, 3)
provinz = Punktekarte("Provinz", anzahl_punktekarten, 8, 6)
kolonie = Punktekarte("Kolonie", anzahl_punktekarten, 11, 10)
punktekarten = [fluch, anwesen, herzogtum, provinz]
punktekarten_ohne_fluch = punktekarten.copy()
punktekarten_ohne_fluch.remove(fluch)

if kolonien:
    punktekarten = punktekarten + [kolonie]


class Aktionskarte:
    def __init__(self, name, anzahl, preis, karte, aktion, kauf, geld, angriff,
                 special):
        self.name = name
        self.anzahl = anzahl
        self.preis = preis
        self.karte = karte
        self.aktion = aktion
        self.kauf = kauf
        self.geld = geld
        self.angriff = angriff
        self.special = special


anzahl_aktionskarten = 10
burggraben = Aktionskarte("Burggraben", anzahl_aktionskarten,
                          2, 2, 0, 0, 0, False, True)
hexe = Aktionskarte("Hexe", anzahl_aktionskarten,
                    5, 2, 0, 0, 0, True, True)
jahrmarkt = Aktionskarte("Jahrmarkt", anzahl_aktionskarten,
                         5, 0, 2, 1, 2, False, False)
holzfaller = Aktionskarte("Holzfäller", anzahl_aktionskarten,
                          3, 0, 0, 1, 2, False, False)
ratsversammlung = Aktionskarte("Ratsversammlung", anzahl_aktionskarten,
                               5, 4, 0, 1, 0, False, True)
dorf = Aktionskarte("Dorf", anzahl_aktionskarten,
                    3, 1, 2, 0, 0, False, False)
laboratorium = Aktionskarte("Laboratorium", anzahl_aktionskarten,
                            5, 2, 1, 0, 0, False, False)
werkstatt = Aktionskarte("Werkstatt", anzahl_aktionskarten,
                         3, 0, 0, 0, 0, False, True)
schmiede = Aktionskarte("Schmiede", anzahl_aktionskarten,
                        4, 3, 0, 0, 0, False, False)
miliz = Aktionskarte("Miliz", anzahl_aktionskarten,
                     4, 0, 0, 0, 2, True, True)
markt = Aktionskarte("Markt", anzahl_aktionskarten,
                     5, 1, 1, 1, 1, False, False)

aktionskarten = [burggraben, hexe, jahrmarkt, holzfaller, ratsversammlung, dorf,
                 laboratorium, werkstatt, schmiede, miliz, markt]

karten_liste = geldkarten + punktekarten + aktionskarten
