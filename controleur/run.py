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

    def deroulement_d_une_ronde(self):
        #Tri des joueurs
        if self.nombre_ronde == 1:
            liste_triee = ""
            self.joueurs_tournoi.sort(key=lambda x: x.classement_elo, reverse=True)
            for joueur in self.joueurs_tournoi:
                liste_triee += joueur.nom+", "
            print("le classement est : "+liste_triee)
        elif int(self.nombre_ronde) > 1:
            liste_triee = ""
            self.joueurs_tournoi.sort(key=lambda x: x.points_tournoi, reverse=True)
            for joueur in self.joueurs_tournoi:
                liste_triee += joueur.nom+", "
            print("le classement est : "+liste_triee)
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
