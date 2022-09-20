
class Ronde:
    """Contient la liste des instances des matches du tour"""

    def __init__(self, nom, date_heure_debut_du_match):
        self.nom_de_la_ronde = nom
        self.date_heure_debut_du_match = date_heure_debut_du_match
        self.date_heure_fin_du_match = ""
        self.liste_matchs = []
        self.resultat_matchs = []

    def __str__(self):
        match1, match2, match3, match4 = self.liste_matchs
        print(match1.__str__)
        print(match2.__str__)
        print(match3.__str__)
        print(match4.__str__)
        # print_match += self.nom_de_la_ronde + " qui a commence à " + str(self.date_heure_debut_du_match) + \
        # " a vu se derouler le match : entre " match.joueur1 + " et " + match.joueur2 + ". "
        # return str(print_match)
