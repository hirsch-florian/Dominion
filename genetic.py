from karten import *
from strategie import *
import pandas as pd
from random import randint, uniform

pop_anzahl = 4
generationen = 100
runden_pro_pop = 1
spieler_pro_spiel = 4
beste = 0
mutation = 5


def gewichtete_auswahl(strategie_gewertet_df: pd.DataFrame) -> \
        StrategiePunkteGeld:
    gesamt_fitness = uniform(0, sum(strategie_gewertet_df["fitness"]))
    while True:
        index = randint(0, len(strategie_gewertet_df) - 1)
        if float(strategie_gewertet_df.iloc[index].fitness) > gesamt_fitness:
            return strategie_gewertet_df.iloc[index].strategie
        else:
            gesamt_fitness -= strategie_gewertet_df.iloc[index].fitness


def fortpflanzung(strategie1: StrategiePunkteGeld,
                  strategie2: StrategiePunkteGeld,
                  generation: int, nummer: int) -> StrategiePunkteGeld:
    strategie_neu = StrategiePunkteGeld(str(generation) + "." + str(nummer))

    if strategie1.kupfer_kauf != strategie2.kupfer_kauf or \
            randint(1, mutation) == 1:
        strategie_neu.random_kupfer_kauf()
    else:
        strategie_neu.kupfer_kauf = strategie1.kupfer_kauf

    if kolonien:
        strategie_neu.kolonie_ab = \
            round((strategie1.kolonie_ab + strategie2.kolonie_ab)/2)
        if randint(1, mutation) == 1:
            strategie_neu.random_kolonie_ab()

    strategie_neu.provinz_ab = \
        round((strategie1.provinz_ab + strategie2.provinz_ab) / 2)
    if randint(1, mutation) == 1:
        strategie_neu.random_provinz_ab()
    strategie_neu.herzogtum_ab = \
        round((strategie1.herzogtum_ab + strategie2.herzogtum_ab) / 2)
    if randint(1, mutation) == 1:
        strategie_neu.random_herzogtum_ab()
    strategie_neu.anwesen_ab = \
        round((strategie1.anwesen_ab + strategie2.anwesen_ab) / 2)
    if randint(1, mutation) == 1:
        strategie_neu.random_anwesen_ab()

    return strategie_neu


def neue_strategien_list(strategie_gewertet_df: pd.DataFrame, gen: int) \
        -> list:
    neue_strategien = []
    for nummmer in range(pop_anzahl - beste):
        strategie1 = gewichtete_auswahl(strategie_gewertet_df)
        strategie2 = gewichtete_auswahl(strategie_gewertet_df)
        neue_strategie = fortpflanzung(strategie1, strategie2, gen, nummmer)
        neue_strategien.append(neue_strategie)

    strategie_gewertet_df = \
        strategie_gewertet_df.sort_values("fitness", ascending=False)
    rangliste = []
    for top_n in range(beste):
        neue_strategie = strategie_gewertet_df.iloc[top_n].strategie
        neue_strategien.append(neue_strategie)
        rangliste.append(neue_strategie.name)
        print(vars(neue_strategie).values(),
              "Top" + str(top_n) + " Gen " + str(gen))
    # print(rangliste)

    if len(neue_strategien) != pop_anzahl:
        print("FUCK")

    return neue_strategien


def strategien_gewertet_df_ausgeben(df):
    for index in range(len(df)):
        strategie = df.iloc[index].strategie
        fitness = df.iloc[index].fitness
        ausgabe = vars(strategie)
        ausgabe.update({"fitness": fitness})
        print(ausgabe)


def main():
    for gen in range(generationen):
        print(gen)
        if gen == 0:
            spieler_df = erstellen_spieler_df(pop_anzahl)
        else:
            strategien_liste = neue_strategien_list(strategie_gewertet_df, gen)
            spieler_df = spieler_df_aus_strategien_liste(len(strategien_liste),
                                                         strategien_liste)

        strategie_gewertet_df = \
            mehrere_spiele_mehrere_spieler(spieler_df,
                                           spieler_pro_spiel,
                                           runden_pro_pop)
        strategien_gewertet_df_ausgeben(strategie_gewertet_df)


if __name__ == '__main__':
    main()
