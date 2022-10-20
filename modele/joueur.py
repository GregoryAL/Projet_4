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
        """ Sérialise le joueur """
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "date_de_naissance": self.date_de_naissance,
            "sexe": self.sexe,
            "classement_elo": self.classement_elo
        }

    def serialisation_participant(self, points_tournoi):
        """ Sérialise le joueur et ajoute les points tournoi """
        return {
            "nom": self.nom,
            "prenom": self.prenom,
            "date_de_naissance": self.date_de_naissance,
            "sexe": self.sexe,
            "classement_elo": self.classement_elo,
            "points_tournoi": points_tournoi
        }

    def __str__(self):
        """ Affichage personnalisé du str joueur """
        return self.prenom + " " + self.nom + " | classement elo : " + str(self.classement_elo)
