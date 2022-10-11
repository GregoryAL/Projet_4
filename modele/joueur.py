class Joueur:
    """Classe du Joueur"""

    def __init__(self, nom, prenom, date_de_naissance,
                 sexe, classement_elo):
        """Le joueur a un nom, un prénom, une date de naissance,
        un sexe, un classement elo, un classement pendant un tournoi,
        un indice unique de joueur pendant un tournoi"""

        self.nom = nom
        self.prenom = prenom
        self.date_de_naissance = date_de_naissance
        self.sexe = sexe
        self.classement_elo = classement_elo

    def serialisation_joueur(self):
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "date_de_naissance": self.date_de_naissance,
            "sexe": self.sexe,
            "classement_elo": self.classement_elo
        }

    def __str__(self):
        return self.prenom + " " + self.nom + " | classement elo : " + str(self.classement_elo)
