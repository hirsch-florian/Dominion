from random import shuffle, randint
from karten import *
import pandas as pd

original_stapel = [karte.anzahl for karte in karten_liste]


class StrategiePunkteGeld:
    def __init__(self, name, kupfer_kauf=0, kolonie_ab=0, provinz_ab=0,
                 herzogtum_ab=0, anwesen_ab=0, kein_silber_ab=0,
                 kein_gold_ab=0, kein_platin_ab=0):
        self.name = name
        self.kupfer_kauf = kupfer_kauf
        self.kolonie_ab = kolonie_ab
        self.provinz_ab = provinz_ab
        self.herzogtum_ab = herzogtum_ab
        self.anwesen_ab = anwesen_ab
        self.kein_silber_ab = kein_silber_ab
        self.kein_gold_ab = kein_gold_ab
        self.kein_platin_ab = kein_platin_ab

    def random_kupfer_kauf(self):
        self.kupfer_kauf = bool(randint(0, 1))

    def random_kolonie_ab(self):
        if kolonien:
            self.kolonie_ab = randint(0, 30)
        else:
            self.kolonie_ab = 1000

    def random_kein_platin_ab(self):
        if kolonien:
            self.kein_platin_ab = randint(0, 30)
        else:
            self.kein_platin_ab = 1000

    def random_provinz_ab(self):
        if kolonien:
            self.provinz_ab = randint(0, anzahl_punktekarten)
        else:
            self.provinz_ab = randint(0, 30)

    def random_herzogtum_ab(self):
        self.herzogtum_ab = randint(0, anzahl_punktekarten)

    def random_anwesen_ab(self):
        self.anwesen_ab = randint(0, anzahl_punktekarten)


class Aktiviert:
    def __init__(self, zug_nummer, anzahl_endstapel):
        self.zug_nummer = zug_nummer
        self.anzahl_endstapel = anzahl_endstapel

    def random(self, zugmin=0, zugmax=max_zug, nmin=0,
               nmax=anzahl_punktekarten):
        self.zug_nummer = randint(zugmin, zugmax)
        self.anzahl_endstapel = randint(nmin, nmax)

    def aktiv(self, runde: int, wichtigster_stapel: Punktekarte) -> bool:
        if runde >= self.zug_nummer or \
                wichtigster_stapel.anzahl <= self.anzahl_endstapel:
            return True
        return False


class PunkteGeld:
    def __init__(self, name, kupfer_kauf, go_ko, pl_ko, go_pr,
                 si_he, ku_an, pl_pr, go_he, si_an, pl_he, go_an, pl_an):
        #         go_ko: Aktiviert, pl_ko: Aktiviert, go_pr: Aktiviert,
        #         si_he: Aktiviert, ku_an: Aktiviert, pl_pr: Aktiviert,
        #         go_he: Aktiviert, si_an: Aktiviert, pl_he: Aktiviert,
        #         go_an: Aktiviert, pl_an: Aktiviert):
        self.name = name
        self.kupfer_kauf = kupfer_kauf
        self.go_ko = go_ko
        self.pl_ko = pl_ko
        self.go_pr = go_pr
        self.si_he = si_he
        self.ku_an = ku_an
        self.pl_pr = pl_pr
        self.go_he = go_he
        self.si_an = si_an
        self.pl_he = pl_he
        self.go_an = go_an
        self.pl_an = pl_an

    def random_go_ko(self):




class StrategieGewertet:
    def __init__(self, strategie, fitness):
        self.strategie = strategie
        self.fitness = fitness


"""
test0 = StrategiePunkteGeld("test1", False, 10, 5, 2)
test1 = StrategiePunkteGeld("test2", True, 8, 8, 4)
test2 = StrategiePunkteGeld("test3", True, 0, 12, 12)
test3 = StrategiePunkteGeld("test4", False, 0, 0, 0)
test4 = StrategiePunkteGeld("test1", False, 10, 5, 2)
test5 = StrategiePunkteGeld("test2", True, 8, 8, 4)
test6 = StrategiePunkteGeld("test3", True, 0, 12, 12)
test7 = StrategiePunkteGeld("test4", False, 0, 0, 0)
test8 = StrategiePunkteGeld("test1", False, 10, 5, 2)
test9 = StrategiePunkteGeld("test2", True, 8, 8, 4)
test10 = StrategiePunkteGeld("test3", True, 0, 12, 12)
test11 = StrategiePunkteGeld("test4", False, 0, 0, 0)
"""


class Spieler:
    def __init__(self, name, nachziehstapel, ablagestapel, handkarten,
                 strategie, punkte, punktedeck, zug_nummer,
                 metapunkte=0, gespielt=0, metapunkte_pro_spiel=0):
        self.name = name
        self.nachziehstapel = nachziehstapel
        self.ablagestapel = ablagestapel
        self.handkarten = handkarten
        self.strategie = strategie
        self.punkte = punkte
        self.punktedeck = punktedeck
        self.zug_nummer = zug_nummer
        self.metapunkte = metapunkte
        self.gespielt = gespielt
        self.metapunkte_pro_spiel = metapunkte_pro_spiel


def reset_karten():
    for karten_index in range(len(karten_liste)):
        karten_liste[karten_index].anzahl = original_stapel[karten_index]
    if platin in karten_liste and kolonie in karten_liste:
        print("yes")


# erstellung des ersten decks mit 3 anwesen und 7 kupfer
def neues_deck() -> list:
    deck = 7 * [kupfer] + 3 * [anwesen]
    shuffle(deck)
    # ausgabe(deck)
    return deck


# ziehen einer karte
# inklusive check, ob der nachziehstapel existiert und eventuellem mischen
def karte_ziehen(nachziehstapel: list, ablagestapel: list) -> (
        list, list, object):
    if not nachziehstapel:
        nachziehstapel = ablagestapel.copy()
        shuffle(nachziehstapel)
        ablagestapel.clear()
        # ausgabe(nachziehstapel)
    neue_karte = nachziehstapel[len(nachziehstapel) - 1]
    nachziehstapel.pop()

    return nachziehstapel, ablagestapel, neue_karte


# ziehen von 5 karten am ende eines zuges
def nachziehen(spieler: Spieler) -> Spieler:
    spieler.handkarten = [[], [], []]
    for _ in range(5):
        spieler.nachziehstapel, \
        spieler.ablagestapel, \
        neue_karte = karte_ziehen(spieler.nachziehstapel,
                                  spieler.ablagestapel)
        index_karte = karte_zuordnen(neue_karte)
        spieler.handkarten[index_karte].append(neue_karte)

    return spieler


# eine gegebene karte wird den drei gruppen aktion 0, geld 1, punkte 2
# zugeordnet
# es wird nur der gegebene wert zurückgegeben und kann als index benutzt werden
def karte_zuordnen(karte) -> int:
    if type(karte).__name__ == "aktionskarte":
        return 0
    if type(karte).__name__ == "geldkarte":
        return 1
    if type(karte).__name__ == "punktekarte":
        return 2


"""
# überprüfen, ob es noch karten gibt, die mehr aktionen ermöglichen
def noch_aktionen(handkarten_aktionen) -> bool:
    max_aktionen_wert = max(handkarten_aktionen[i].aktion
                            for i in range(len(handkarten_aktionen)))
    if max_aktionen_wert != 0:
        return True
    return False


# überprüfen, ob es noch karten gibt, die mehr karten ermöglichen
def noch_karten(handkarten_aktionen) -> bool:
    index_karten = 2
    max_karten_wert = max(handkarten_aktionen[i].karte
                          for i in range(len(handkarten_aktionen)))
    if max_karten_wert != 0:
        return True
    return False


# finden der karte, die die maximale anzahl an neuen karten
# ermöglicht
# ausgegeben wird der index in der übergebenen liste
def max_karten(handkarten_aktionen) -> int:
    zu_spielen = []
    max_karten_wert = max(handkarten_aktionen[i].karte
                          for i in range(len(handkarten_aktionen)))
    for index in range(len(handkarten_aktionen)):
        if handkarten_aktionen[index].karte == max_karten_wert:
            zu_spielen.append(index)

    return zu_spielen[0]


def max_aktionen(handkarten_aktionen) -> object:
    zu_spielen = []
    max_aktionen_wert = max(handkarten_aktionen[i].aktion
                            for i in range(len(handkarten_aktionen)))
    for karte in handkarten_aktionen:
        if karte.aktion == max_aktionen_wert:
            zu_spielen.append(karte)

    if len(zu_spielen) > 1:
        zu_spielen = [max_karten(zu_spielen)]

    return zu_spielen[0]"""


# aus strategie und zugnummer wird ein warenkorb zusammengestellt, der die
# wunschkarten enthält und deren kaufpriorität mittels preis wiedergibt
def personalisierter_warenkorb(zug_nummer, strategie: StrategiePunkteGeld) \
        -> list:
    warenkorb = []
    if kolonien:
        zu_messende_anzahl = kolonie.anzahl
    else:
        zu_messende_anzahl = provinz.anzahl
    warenkorb.extend(geldkarten)
    if not strategie.kupfer_kauf:
        if kupfer in warenkorb: warenkorb.remove(kupfer)

    if kolonien:
        if zug_nummer >= strategie.kolonie_ab and karte_vorhanden(kolonie):
            warenkorb.append(kolonie)
        if zu_messende_anzahl <= strategie.provinz_ab and \
                karte_vorhanden(provinz):
            warenkorb.append(provinz)
            if platin in warenkorb: warenkorb.remove(platin)
    else:
        if zug_nummer >= strategie.provinz_ab and karte_vorhanden(provinz):
            warenkorb.append(provinz)
    if zu_messende_anzahl <= strategie.herzogtum_ab and \
            karte_vorhanden(herzogtum):
        warenkorb.append(herzogtum)
        if gold in warenkorb: warenkorb.remove(gold)
        if platin in warenkorb: warenkorb.remove(platin)
    if zu_messende_anzahl <= strategie.anwesen_ab and karte_vorhanden(anwesen):
        warenkorb.append(anwesen)
        if silber in warenkorb: warenkorb.remove(silber)
        if gold in warenkorb: warenkorb.remove(gold)
        if platin in warenkorb: warenkorb.remove(platin)

    return warenkorb


# der geldwert aller geldkarten wird zusammengezählt
def geld_spielen(handkarten_geld) -> int:
    geld = 0
    for karte in handkarten_geld:
        geld += karte.geld
    return geld


"""
# von verfügbaren geld und käufen werden die bestmöglichen geldkarten gekauft
def geld_kaufen(kauf, geld) -> list:
    gekauft = []
    geldkarten = [gold, silber, kupfer]
    if kolonien: geldkarten = [platin] + geldkarten

    for _ in range(kauf):
        neue_karte, geld = teuerste_kaufen(geldkarten, geld)
        if neue_karte:
            gekauft.append(neue_karte)

    return gekauft
"""


# die übergebene karte wird vom vorratsstapel genommen, der vorratsstapel wird
# also um 1 weniger
def karte_nehmen(karte):
    karte.anzahl -= 1
    return


# aus elementen der gleichen klasse wir ein dataframe gemacht
def dataframe_erstellung(liste_instanzen) -> pd.DataFrame:
    dictionary = [vars(i) for i in liste_instanzen]
    df = pd.DataFrame(dictionary)  # .set_index("name")
    for key in df.keys():
        df[key] = df[key].astype("object")
    return df


# aus einer übergebenen liste von möglichen käufen und dem verfügbaren geld wird
# die teuerst mögliche karte, für die das geld reicht, vom vorratsstapel
# entfernt und zurückgegeben
# wenn keine der gewünschten karten gekauft werden kann, wird als karte None
# wiedergegeben, dies muss entsprechend gehändelt werden
def teuerste_kaufen(karten: list, geld: int) -> (object, int):
    kaufbar = []
    for karte in karten:
        if karte.preis <= geld and karte_vorhanden(karte):
            kaufbar.append(karte)

    if kaufbar:
        max_preis = max(kaufbar[i].preis for i in range(len(kaufbar)))
    else:
        return None, geld

    geld -= max_preis

    for karte in kaufbar:
        if karte.preis == max_preis:
            karte_nehmen(karte)
            return karte, geld


"""
# von verfügbaren geld und käufen werden die bestmöglichen punktekarten gekauft
def punkte_kaufen(kauf, geld) -> list:
    gekauft = []
    punktekarten = [provinz, herzogtum, anwesen]
    if kolonien: punktekarten = [kolonie] + punktekarten

    for _ in range(kauf):
        neue_karte, geld = teuerste_kaufen(punktekarten_ohne_fluch, geld)
        if neue_karte:
            gekauft.append(neue_karte)

    return gekauft
"""


# aus dem personalisierten warenkorb wird so oft die teuerste karte gekauft, wie
# käufe und geld dafür ausreichen, der warenkorb hängt von strategie und
# zugnummer ab
def kaufen(zug_nummer, strategie: StrategiePunkteGeld, kauf, geld) -> list:
    warenkorb = personalisierter_warenkorb(zug_nummer, strategie)
    gekauft = []
    urgeld = geld
    # if geld >= 11 and (kolonie not in warenkorb):
    #    print("Platin")
    for _ in range(kauf):
        neue_karte, geld = teuerste_kaufen(warenkorb, geld)
        if neue_karte:
            gekauft.append(neue_karte)
            print(neue_karte.name, urgeld)

    return gekauft


def ausgabe_liste(liste: list):
    namen = []
    if liste:
        for karte in liste:
            namen.append(karte.name)
        # print(namen)
    return


def ausgabe_strategie(strategie: StrategiePunkteGeld):
    print(vars(strategie))


def zug(spieler: Spieler) -> Spieler:
    aktion = 1
    kauf = 1
    geld = 0

    geld += geld_spielen(spieler.handkarten[1])

    gekauft = kaufen(spieler.zug_nummer, spieler.strategie, kauf, geld)

    for i in range(3):
        spieler.ablagestapel.extend(spieler.handkarten[i])
    spieler.ablagestapel.extend(gekauft)

    spieler = nachziehen(spieler)

    return spieler


# sammelt alle karten eines spielers und gibt dessen punktewert sowie die
# punktekarten als liste zurück
def punkte_auswerten(spieler) -> Spieler:
    deck = []
    spieler.punktedeck = []
    spieler.punkte = 0
    deck.extend(spieler.nachziehstapel)
    deck.extend(spieler.ablagestapel)
    for i in range(3):
        deck.extend(spieler.handkarten[i])

    for karte in deck:
        index = karte_zuordnen(karte)
        if index == 2:
            spieler.punktedeck.append(karte)

    for karte in spieler.punktedeck:
        spieler.punkte += karte.punkte

    return spieler


# prüft, ob eine karte noch zu kaufen ist und gibt es als bool zurück
def karte_vorhanden(karte) -> bool:
    if karte.anzahl > 0:
        return True
    return False


def erstellen_strategieliste_zufall(anzahl_spieler: int) -> list:
    strategieliste = []
    for spieler_nummer in range(anzahl_spieler):
        strategie = StrategiePunkteGeld(str(spieler_nummer))
        strategie.random_kupfer_kauf()
        strategie.random_kolonie_ab()
        strategie.random_provinz_ab()
        strategie.random_herzogtum_ab()
        strategie.random_anwesen_ab()
        strategieliste.append(strategie)
    return strategieliste


"""
def erstellen_strategieliste() -> list:
    strategieliste = [test0, test1, test2, test3]
    return strategieliste
"""


def erstellen_spielerliste(anzahl_spieler: int, strategieliste,
                           zufall=False) -> list:
    spieler_liste = []
    # strategieliste = erstellen_strategieliste()
    if zufall:
        strategieliste = erstellen_strategieliste_zufall(anzahl_spieler)
    for spieler_nummer in range(anzahl_spieler):
        spieler_liste.append(Spieler(strategieliste[spieler_nummer].name,
                                     [0], [0], [0],
                                     strategieliste[spieler_nummer],
                                     0, [0], 0))
    return spieler_liste


def spiel_mehrere_spieler(spieler_df: pd.DataFrame) -> pd.DataFrame:
    reset_karten()
    for spieler_nummer in spieler_df.index:
        # print(spieler_nummer)
        # print(spieler_df.loc[spieler_nummer])
        spieler_df.at[spieler_nummer, "nachziehstapel"] = neues_deck()
        spieler_df.loc[spieler_nummer, "ablagestapel"] = []
        spieler_df.loc[spieler_nummer] = \
            nachziehen(spieler_df.loc[spieler_nummer])
        spieler_df.loc[spieler_nummer] = \
            punkte_auswerten(spieler_df.loc[spieler_nummer])

    if kolonien:
        wichtigster_stapel = kolonie
    else:
        wichtigster_stapel = provinz

    while True:
        print(spieler_df.iloc[0].zug_nummer)
        for spieler_nummer in spieler_df.index:
            spieler_df.loc[spieler_nummer, "zug_nummer"] += 1
            spieler_df.loc[spieler_nummer] = \
                zug(spieler_df.loc[spieler_nummer])

            spieler_df.loc[spieler_nummer] = \
                punkte_auswerten(spieler_df.loc[spieler_nummer])

            """print(spieler_df.loc[spieler_nummer].strategie.name, " hat ",
                  spieler_df.loc[spieler_nummer].punkte," Punkte in Zug",
                  spieler_df.loc[spieler_nummer].zug_nummer)"""

            if wichtigster_stapel.anzahl == 0:
                return spieler_df


def auswertung_spiel(spieler_df: pd.DataFrame) -> pd.DataFrame:
    spieler_df_sortiert = spieler_df.sort_values("punkte", ascending=False)
    belohnung = [4, 2, 1, 0]
    spieler_indizes = spieler_df_sortiert.index
    for spieler_index in range(len(spieler_indizes)):
        spieler_df_sortiert.loc[spieler_indizes[spieler_index],
                                "metapunkte"] += belohnung[spieler_index]
        spieler_df_sortiert.loc[spieler_indizes[spieler_index], "gespielt"] += 1
    return spieler_df_sortiert


def spieler_df_aus_strategien_liste(anzahl_spieler: int,
                                    strategien_liste: list) -> pd.DataFrame:
    spieler_liste = erstellen_spielerliste(anzahl_spieler, strategien_liste)
    spieler_df = dataframe_erstellung(spieler_liste)
    return spieler_df


def erstellen_spieler_df(anzahl_spieler: int) -> pd.DataFrame:
    spieler_liste = erstellen_spielerliste(anzahl_spieler, [], zufall=True)
    spieler_df = dataframe_erstellung(spieler_liste)
    return spieler_df


def mehrere_spiele_mehrere_spieler(spieler_df, spieler_pro_spiel,
                                   anzahl_runden) -> pd.DataFrame:
    for runde in range(anzahl_runden):
        spiel_indizes = []
        alle_spieler = list(spieler_df.index)
        for _ in range(spieler_pro_spiel):
            neuer_spieler_nummer = randint(0, len(alle_spieler) - 1)
            spiel_indizes.append(alle_spieler[neuer_spieler_nummer])
            alle_spieler.pop(neuer_spieler_nummer)

        spiel_df = spieler_df.loc[spiel_indizes]
        spiel_df = spiel_mehrere_spieler(spiel_df)
        spiel_df = auswertung_spiel(spiel_df)
        for index in spiel_df.index:
            spieler_df.loc[index] = spiel_df.loc[index]
        print(runde)

    for spieler_index in spieler_df.index:
        spieler_df.loc[spieler_index, "metapunkte_pro_spiel"] = \
            spieler_df.loc[spieler_index, "metapunkte"] / \
            spieler_df.loc[spieler_index, "gespielt"]

    spieler_df = spieler_df.sort_values("metapunkte_pro_spiel", ascending=False)

    # print(spieler_df[["metapunkte", "gespielt", "metapunkte_pro_spiel"]])
    strategie_gewertet_liste = []
    for index in spieler_df.index:
        neue_strategie = \
            StrategieGewertet(spieler_df.loc[index, "strategie"],
                              spieler_df.loc[
                                  index, "metapunkte_pro_spiel"] ** 3)
        strategie_gewertet_liste.append(neue_strategie)

    strategie_gewertet_df = dataframe_erstellung(strategie_gewertet_liste)

    # print(strategie_gewertet_df)

    return strategie_gewertet_df


if __name__ == '__main__':
    # mehrere_spiele()
    # spiel()
    # spiel_mehrere_spieler(4)
    anfangsspieler_df = erstellen_spieler_df(4)
    mehrere_spiele_mehrere_spieler(anfangsspieler_df, 4, 1)
