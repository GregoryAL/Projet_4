""" Point d'entrée du contrôleur"""
from modele import tournoi
from modele import match
from modele import ronde
from modele import joueurs
import datetime
import random


class Controleur:
    """ contrôleur general """

    def __init__(self, type_de_tournoi="TournoiSuisse", vue=""):
        """ A un type de déroulement du tournoi et une vue. """
        self.type_de_tournoi = type_de_tournoi
        self.vue = vue

    def creation_du_tournoi(self):
        """ Creation d'un tournoi en utilisant les paramètres utilisateurs"""
        # données d'un tournoi statique
        tournoi_de_test_statique = tournoi.Tournoi("tournoi de test",
                                                   "lieu de test",
                                                   "01/01/22",
                                                   "blitz",
                                                   8)
        return tournoi_de_test_statique

    def ajout_des_joueurs(self):
        """ Ajout des joueurs """
        # Ajout des 8 joueurs statique
        player1 = joueurs.Joueur("Nom1", "prénom1", "11/11/11", "M", 1650)
        player2 = joueurs.Joueur("Nom2", "prénom2", "10/10/10", "F", 1435)
        player3 = joueurs.Joueur("Nom3", "prénom3", "9/9/9", "U", 1983)
        player4 = joueurs.Joueur("Nom4", "prénom4", "08/08/08", "M", 1945)
        player5 = joueurs.Joueur("Nom5", "prénom5", "04/05/06", "F", 1345)
        player6 = joueurs.Joueur("Nom6", "prénom6", "11/5/11", "M", 1580)
        player7 = joueurs.Joueur("Nom7", "prénom7", "10/9/10", "F", 1415)
        player8 = joueurs.Joueur("Nom8", "prénom8", "9/4/9", "U", 1953)
        liste_joueurs = [player1, player2, player3, player4, player5,
                         player6, player7, player8]
        return liste_joueurs

    def creation_des_matchs_methode_suisse(self, numero_ronde,
                                           liste_participant):
        # Tri des joueurs
        if numero_ronde == 1:
            liste_triee = ""
            liste_participant.sort(key=lambda x: x.classement_elo,
                                   reverse=True)
            for joueur in liste_participant:
                liste_triee += joueur.nom+", "
            print("le classement est : "+liste_triee)
        elif numero_ronde > 1:
            liste_triee = ""
            liste_participant.sort(key=lambda x: x.points_tournoi,
                                   reverse=True)
            for joueur in liste_participant:
                liste_triee += joueur.nom+", "
            print("le classement est : "+liste_triee)
        # Creation des paires
        if len(liste_participant) == 8:
            match1 = match.Match(liste_participant[0], liste_participant[4])
            match2 = match.Match(liste_participant[1], liste_participant[5])
            match3 = match.Match(liste_participant[2], liste_participant[6])
            match4 = match.Match(liste_participant[3], liste_participant[7])
            ronde_actuelle = ronde.Ronde("round"+str(numero_ronde),
                                         datetime.datetime.now())
            ronde_actuelle.liste_matchs = [match1, match2, match3, match4]
            return ronde_actuelle

    def deroulement_d_une_ronde(self, numero_de_ronde, liste_de_joueur):
        """ Mécanisme de fonctionnement d'une ronde"""
        # Creation de l'objet instancié tournoi nécessaire
        ronde_actuelle = Controleur.\
            creation_des_matchs_methode_suisse(self,
                                               numero_de_ronde,
                                               liste_de_joueur)
        for match in ronde_actuelle.liste_matchs:
            print(match.joueur1.nom + " affronte " + match.joueur2.nom)
            vainqueur = random.choice([match.joueur1, match.joueur2, "nul"])
            if vainqueur == match.joueur1:
                print(match.joueur1.nom + " a gagné contre " +
                      match.joueur2.nom)
                match.joueur1.points_tournoi += 1
                match.joueur2.points_tournoi += 0
                resultat_match = ([match.joueur1, "victoire"],
                                  [match.joueur2, "défaite"])
            elif vainqueur == match.joueur2:
                print(match.joueur2.nom + " a gagné contre " +
                      match.joueur1.nom)
                match.joueur2.points_tournoi += 1
                match.joueur1.points_tournoi += 0
                resultat_match = ([match.joueur1, "défaite"],
                                  [match.joueur2, "victoire"])
            elif vainqueur == "nul":
                print("C'est un match nul")
                match.joueur1.points_tournoi += 0.5
                match.joueur2.points_tournoi += 0.5
                resultat_match = ([match.joueur1, "nul"],
                                  [match.joueur2, "nul"])
        for participant in liste_de_joueur:
            print(participant.nom + " a maintenant " +
                  str(participant.points_tournoi) +
                  " point(s).")
        return resultat_match
