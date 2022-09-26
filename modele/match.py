class Match:
    """ Match entre 2 joueurs dans une ronde du tournoi """

    def __init__(self, joueur1, joueur2):
        """ Un match possède un tuple (composé d'un
        identifiant pointant vers le joueur 1, le score du joueur
        1), et un autre tuple (avec un identifiant pointant vers
        le joueur 2, le score du joueur 2 """
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.resultat_joueur1 = ""
        self.resultat_joueur2 = ""
        self.tuple_match = ([self.joueur1, self.resultat_joueur1], [self.joueur2, self.resultat_joueur2])

    def __str__(self):
        return self.joueur1, " a obtenu : ", self.resultat_joueur1, self.joueur2, " a obtenu : ", self.resultat_joueur2


