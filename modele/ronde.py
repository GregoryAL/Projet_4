
class Ronde:
    """Contient la liste des instances des matches du tour"""

    def __init__(self, nom, date_heure_debut_du_match):
        self.nom_de_la_ronde = nom
        self.date_heure_debut_du_match = date_heure_debut_du_match
        self.date_heure_fin_du_match = ""
        self.liste_matchs = []
