class Match:
    """ Match entre 2 joueurs dans une ronde du tournoi """

    def __init__(self, joueur1, joueur2):
        """ Un match possède le nom de la ronde dans laquelle il se déroule, un numéro, une heure et une date de début,
         une heure et une date de fin, un tuple (composé d'un identifiant pointant vers le joueur 1, le score du
         joueur 1), et un autre tuple (avec un identifiant pointant vers le joueur 2, le score du joueur 2), un
         identifiant unique composé du nom de la ronde et de son numéro de match de la ronde. Il possède également une
         méthode d'ajout de point pour un joueur en fonction du résultat du match. """
        self.joueur1 = joueur1
        self.joueur2 = joueur2






