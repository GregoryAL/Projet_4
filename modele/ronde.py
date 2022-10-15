

class Ronde:
    """Contient la liste des instances des matches du tour"""

    def __init__(self, nom):
        self.nom_de_la_ronde = nom
        self.date_heure_debut_de_ronde = ""
        self.date_heure_fin_de_ronde = ""
        self.liste_matchs = []

    def serialisation_ronde(self):
        return {
            "nom_de_la_ronde": self.nom_de_la_ronde,
            "date_heure_debut_ronde": self.date_heure_debut_de_ronde,
            "date_heure_fin_ronde": self.date_heure_fin_de_ronde,
            "liste_match": self.liste_matchs
        }
