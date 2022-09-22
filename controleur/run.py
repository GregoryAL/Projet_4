""" Point d'entrée du contrôleur"""
from modele import tournoi
from modele import match
from modele import ronde
from modele import joueurs
import datetime
import random
from vue.vue import Vue



class Controleur:
    """ contrôleur general """

    def __init__(self):
        """ initialise le controleur. """
        self.liste_des_joueurs = ""
        self.instance_de_tournoi = ""
        self.vue_input = Vue

    def affichage_du_menu(self):
        """ Affiche le menu du tournoi, récupère le choix utilisateur et lance la methode correspondante """
        choix_utilisateur = int(Vue.menu(self.vue_input))
        if choix_utilisateur == 1:
            info_instance_tournoi_a_creer = Vue.recuperation_des_informations_du_tournoi(self.vue_input)
            self.instance_de_tournoi = self.creation_du_tournoi(info_instance_tournoi_a_creer)
        elif choix_utilisateur == 2:
            self.instance_de_tournoi.rondes[-1].resultat_matchs = self.recuperation_des_scores(self.instance_de_tournoi.rondes[-1])




    def recuperation_des_scores(self, ronde_en_cours):
        """ Recuperation des scores de la vue pour chaque match d'une ronde """
        for match_a_recupere in ronde_en_cours.liste_matchs:
            match_a_recupere.resultat_joueur1 = Vue.recuperation_des_resultats_d_un_match(match_a_recupere.joueur1)
            match_a_recupere.resultat_joueur2 = Vue.recuperation_des_resultats_d_un_match(match_a_recupere.joueur2)
            match_a_recupere.tuple_match = ([match_a_recupere.joueur1, match_a_recupere.resultat_joueur1],
                                            [match_a_recupere.joueur2, match_a_recupere.resultat_joueur2])
            ronde_en_cours.resultat_matchs = match_a_recupere.tuple_match





    def creation_du_tournoi(self, info_tournoi):
        """ Creation d'un tournoi en utilisant les paramètres utilisateurs"""
        # données d'un tournoi statique
        instance_de_tournoi = tournoi.Tournoi(*info_tournoi)
        return instance_de_tournoi

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
        liste_joueurs = [player1, player2, player3, player4, player5, player6, player7, player8]
        return liste_joueurs

    def classement_des_joueurs(self, liste_participant, facteur_tri):
        if facteur_tri == "classement_elo":
            liste_participant.sort(key=lambda x: x.classement_elo, reverse=True)
        elif facteur_tri == "points_tournoi:":
            liste_participant.sort(key=lambda x: x.points_tournoi, reverse=True)
        return liste_participant


    def creation_des_matchs_methode_suisse(self, numero_ronde, liste_participant):
        # Tri des joueurs
        if numero_ronde == 1:
            liste_participant.sort(key=lambda x: x.classement_elo, reverse=True)
            print("le classement est : ")
            for joueur in liste_participant:
                print(joueurs.Joueur.__str__(joueur))
        elif numero_ronde > 1:
            liste_participant.sort(key=lambda x: x.points_tournoi, reverse=True)
            print("le classement est : ")
            for joueur in liste_participant:
                print(joueurs.Joueur.__str__(joueur))
        # Creation des paires
        if len(liste_participant) == 8:
            match1 = match.Match(liste_participant[0], liste_participant[4])
            match2 = match.Match(liste_participant[1], liste_participant[5])
            match3 = match.Match(liste_participant[2], liste_participant[6])
            match4 = match.Match(liste_participant[3], liste_participant[7])
            ronde_actuelle = ronde.Ronde("round"+str(numero_ronde),
                                         datetime.datetime.now())
            ronde_actuelle.liste_matchs = [match1, match2, match3, match4]
            # print(ronde_actuelle.__str__())
            return ronde_actuelle

    def deroulement_d_une_ronde(self, numero_de_ronde, liste_de_joueur):
        """ Mécanisme de fonctionnement d'une ronde"""
        # Creation de l'objet instancié tournoi nécessaire
        ronde_actuelle = Controleur.creation_des_matchs_methode_suisse(self, numero_de_ronde, liste_de_joueur)
        # pour chaque match de la liste des matchs de la ronde
        for match_de_ronde in ronde_actuelle.liste_matchs:
            # affiche le match en cours
            print(match_de_ronde.joueur1.nom + " affronte " + match_de_ronde.joueur2.nom)
            # determine un vainqueur
            vainqueur = random.choice([match_de_ronde.joueur1, match_de_ronde.joueur2, "nul"])
            # modifie les points de tournoi de chaque joueur en fonction du resultat du match
            if vainqueur == match_de_ronde.joueur1:
                print(match_de_ronde.joueur1.nom + " a gagné contre " + match_de_ronde.joueur2.nom)
                match_de_ronde.resultat_joueur1 = 1
                match_de_ronde.resultat_joueur2 = 0
            elif vainqueur == match_de_ronde.joueur2:
                print(match_de_ronde.joueur2.nom + " a gagné contre " + match_de_ronde.joueur1.nom)
                match_de_ronde.resultat_joueur1 = 0
                match_de_ronde.resultat_joueur2 = 1
            elif vainqueur == "nul":
                print("C'est un match nul")
                match_de_ronde.resultat_joueur1 = 0.5
                match_de_ronde.resultat_joueur2 = 0.5
            match_de_ronde.joueur1.points_tournoi += match_de_ronde.resultat_joueur1
            match_de_ronde.joueur2.points_tournoi += match_de_ronde.resultat_joueur2
            match_de_ronde.match = [[match_de_ronde.joueur1, match_de_ronde.resultat_joueur1],
                                    [match_de_ronde.joueur2, match_de_ronde.resultat_joueur2]]
            ronde_actuelle.resultat_matchs = match.Match.creation_tuple_matchs(match_de_ronde)
        # for participant in liste_de_joueur:
            # print(joueurs.Joueur.__str__(participant))

        return ronde_actuelle
