""" Point d'entrée du contrôleur"""
from modele import match
from modele import ronde
import datetime


class Controleur:
    """ contrôleur general """

    def __init__(self):
        """ A un type de déroulement du tournoi, une liste de joueur et une vue. """
        # Creation du tournoi





# Gestion d'une ronde

class TournoiSuisse:

    def __init__(self, nombre_ronde, joueurs_tournoi):
        self.nombre_ronde = nombre_ronde
        self.joueurs_tournoi = joueurs_tournoi

    def tri_des_joueurs_pour_ronde(self):
        if self.nombre_ronde == 1:
            self.joueurs_tournoi.sort(key=lambda x: x.classement_elo)
        elif self.nombre_ronde > 1:
            self.joueurs_tournoi.sort(key=lambda x: x.points_tournoi)
        else:
            print("erreur")

    def appairage_des_joueurs(self):
        #Tri des joueurs
        if self.nombre_ronde == 1:
            self.joueurs_tournoi.sort(key=lambda x: x.classement_elo, reverse=True)
        elif self.nombre_ronde > 1:
            self.joueurs_tournoi.sort(key=lambda x: x.points_tournoi, reverse=True)
        else:
            print("erreur")
        #Creation des paires
        if len(self.joueurs_tournoi) == 8:
            match1 = match.Match(self.joueurs_tournoi[0], self.joueurs_tournoi[4])
            match2 = match.Match(self.joueurs_tournoi[1], self.joueurs_tournoi[5])
            match3 = match.Match(self.joueurs_tournoi[2], self.joueurs_tournoi[6])
            match4 = match.Match(self.joueurs_tournoi[3], self.joueurs_tournoi[7])
            ronde_actuelle = ronde.Ronde("round"+str(self.nombre_ronde), datetime.datetime.now())
            ronde_actuelle.liste_matchs = [match1, match2, match3, match4]
            return ronde_actuelle
"""
    def Ajout_point(self, vainqueur_match):
        "Méthode ajoutant un point par victoire, un demi point par nul, et 0 point par défaite."

        if self.vainqueur_match == self.id_player_1:
            self.player_1 = (self.id_player_1, 1)
            self.player_2 = (self.id_player_2, 0)

        elif self.vainqueur_match == self.id_player_2:
            self.player_1 = (self.id_player_1, 0)
            self.player_2 = (self.id_player_2, 1)

        elif self.vainqueur_match == "match_nul":
            self.player_1 = (self.id_player_1, 0.5)
            self.player_2 = (self.id_player_2, 0.5)

        else:
            print("Veuillez entrez un vainqueur ou indiquez un match nul")"""