class Joueur:
    """Classe du Joueur"""

    def __init__(self, nom, prenom, date_de_naissance,
                 sexe, classement_elo, points_tournoi=0):
        """Le joueur a un nom, un prénom, une date de naissance,
        un sexe, un classement elo, un classement pendant un tournoi,
        un indice unique de joueur pendant un tournoi"""

        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.sexe = sexe
        self.classement_elo = classement_elo
        self.points_tournoi = points_tournoi

    def serialisation_joueur(self):
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "date_de_naissance": self.date_de_naissance,
            "sexe": self.sexe,
            "classement_elo": self.classement_elo,
            "points_tournoi": self.points_tournoi
        }

    def __str__(self):
        return self.prenom + " " + self.nom + " | nombre de point tournoi : " + \
               str(self.points_tournoi) + " | classement elo : " + str(self.classement_elo)
