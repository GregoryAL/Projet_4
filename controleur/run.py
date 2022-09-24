""" Point d'entrée du contrôleur"""
import sys

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
        self.liste_joueurs = {}
        self.liste_joueurs = self.ajout_des_joueurs()
        self.instance_de_tournoi = ""
        self.vue_input = Vue()


    def affichage_du_menu(self):
        """ Affiche le menu du tournoi, récupère le choix utilisateur et lance la methode correspondante """
        choix_utilisateur = int(Vue.menu(self.vue_input))
        if choix_utilisateur == 1:
            info_instance_tournoi_a_creer = Vue.recuperation_des_informations_du_tournoi(self.vue_input)
            self.instance_de_tournoi = self.creation_du_tournoi(info_instance_tournoi_a_creer)
            return self.instance_de_tournoi
        elif choix_utilisateur == 2:
            print(self.instance_de_tournoi.nombre_de_tour_du_tournoi)
            for numero_de_ronde in range(self.instance_de_tournoi.nombre_de_tour_du_tournoi):
                print(numero_de_ronde)
                ronde_actuelle = self.deroulement_d_une_ronde(numero_de_ronde+1)
                self.instance_de_tournoi.rondes.append(ronde_actuelle)
                print(self.instance_de_tournoi.rondes)
            return self.instance_de_tournoi
        elif choix_utilisateur == 3:
            self.instance_de_tournoi.rondes[-1].resultat_matchs = \
                self.recuperation_des_scores(self.instance_de_tournoi.rondes[-1])
            return self.instance_de_tournoi
        elif choix_utilisateur == 4:
            print(int(self.instance_de_tournoi.nombre_de_tour_du_tournoi))
            print(self.instance_de_tournoi)
        elif choix_utilisateur == 5:
            return choix_utilisateur




    def recuperation_des_scores(self):
        """ Recuperation des scores de la vue pour chaque match d'une ronde """
        for match_a_recupere in self.instance_de_tournoi.rondes[-1].liste_matchs:
            match_a_recupere.resultat_joueur1 = Vue.recuperation_des_resultats_d_un_match(match_a_recupere.joueur1)
            match_a_recupere.resultat_joueur2 = Vue.recuperation_des_resultats_d_un_match(match_a_recupere.joueur2)
            match_a_recupere.tuple_match = ([match_a_recupere.joueur1, match_a_recupere.resultat_joueur1],
                                            [match_a_recupere.joueur2, match_a_recupere.resultat_joueur2])
            self.instance_de_tournoi.rondes[-1].resultat_matchs = match_a_recupere.tuple_match
        return self.instance_de_tournoi





    def creation_du_tournoi(self, info_tournoi):
        """ Creation d'un tournoi en utilisant les paramètres utilisateurs"""
        # Creation d'un objet tournoi avec les informations récupérées par la Vue
        self.instance_de_tournoi = tournoi.Tournoi(info_tournoi["nom_du_tournoi"],
                                                   info_tournoi["lieu_du_tournoi"],
                                                   info_tournoi["date_de_tournoi"],
                                                   info_tournoi["type_de_controle_du_temps"],
                                                   info_tournoi["nombre_de_participant"],
                                                   info_tournoi["nombre_de_tour"],
                                                   info_tournoi["commentaires"])
        # Récuperation de la liste des joueurs avec la Vue
        print(self.instance_de_tournoi.nombre_de_participants)
        for i in range(self.instance_de_tournoi.nombre_de_participants):
            self.instance_de_tournoi.participants.append(random.choice(list(self.liste_joueurs.keys())))
        print(self.instance_de_tournoi.participants)
        return self.instance_de_tournoi


    def ajout_des_joueurs(self):
        """ Ajout des joueurs """
        # Pool de 24 joueurs statiques
        self.liste_joueurs["player01"] = joueurs.Joueur("Nom1", "prénom1", "11/11/11", "M", 1650)
        self.liste_joueurs["player02"] = joueurs.Joueur("Nom2", "prénom2", "10/10/10", "F", 1435)
        self.liste_joueurs["player03"] = joueurs.Joueur("Nom3", "prénom3", "9/9/9", "U", 1983)
        self.liste_joueurs["player04"] = joueurs.Joueur("Nom4", "prénom4", "08/08/08", "M", 1945)
        self.liste_joueurs["player05"] = joueurs.Joueur("Nom5", "prénom5", "04/05/06", "F", 1345)
        self.liste_joueurs["player06"] = joueurs.Joueur("Nom6", "prénom6", "11/5/11", "M", 1580)
        self.liste_joueurs["player07"] = joueurs.Joueur("Nom7", "prénom7", "10/9/10", "F", 1415)
        self.liste_joueurs["player08"] = joueurs.Joueur("Nom8", "prénom8", "9/4/9", "U", 1953)
        self.liste_joueurs["player11"] = joueurs.Joueur("Nom11", "prénom11", "11/11/11", "M", 1450)
        self.liste_joueurs["player12"] = joueurs.Joueur("Nom12", "prénom12", "10/10/10", "F", 1535)
        self.liste_joueurs["player13"] = joueurs.Joueur("Nom13", "prénom13", "9/9/9", "U", 1783)
        self.liste_joueurs["player14"] = joueurs.Joueur("Nom14", "prénom14", "08/08/08", "M", 1245)
        self.liste_joueurs["player15"] = joueurs.Joueur("Nom15", "prénom15", "04/05/06", "F", 1545)
        self.liste_joueurs["player16"] = joueurs.Joueur("Nom16", "prénom16", "11/5/11", "M", 1380)
        self.liste_joueurs["player17"] = joueurs.Joueur("Nom17", "prénom17", "10/9/10", "F", 1615)
        self.liste_joueurs["player18"] = joueurs.Joueur("Nom18", "prénom18", "9/4/9", "U", 1153)
        self.liste_joueurs["player21"] = joueurs.Joueur("Nom21", "prénom21", "11/11/11", "M", 1250)
        self.liste_joueurs["player22"] = joueurs.Joueur("Nom22", "prénom22", "10/10/10", "F", 1335)
        self.liste_joueurs["player23"] = joueurs.Joueur("Nom23", "prénom23", "9/9/9", "U", 1483)
        self.liste_joueurs["player24"] = joueurs.Joueur("Nom24", "prénom24", "08/08/08", "M", 1545)
        self.liste_joueurs["player25"] = joueurs.Joueur("Nom25", "prénom25", "04/05/06", "F", 1645)
        self.liste_joueurs["player26"] = joueurs.Joueur("Nom26", "prénom26", "11/5/11", "M", 1780)
        self.liste_joueurs["player27"] = joueurs.Joueur("Nom27", "prénom27", "10/9/10", "F", 1815)
        self.liste_joueurs["player28"] = joueurs.Joueur("Nom28", "prénom28", "9/4/9", "U", 1053)
        return self.liste_joueurs

    def classement_des_joueurs(self, liste_participant, facteur_tri):
        if facteur_tri == "classement_elo":
            liste_participant.sort(key=lambda x: x.classement_elo, reverse=True)
        elif facteur_tri == "points_tournoi:":
            liste_participant.sort(key=lambda x: x.points_tournoi, reverse=True)
        return liste_participant


    def creation_des_matchs_methode_suisse(self, numero_ronde):
        # Tri des joueurs
        if numero_ronde == 1:
            self.instance_de_tournoi.participants.sort(key=lambda x: x.classement_elo, reverse=True)
            print("le classement est : ")
            for joueur in self.instance_de_tournoi.participants:
                print(joueurs.Joueur.__str__(joueur))
        elif numero_ronde > 1:
            self.instance_de_tournoi.participants.sort(key=lambda x: x.points_tournoi, reverse=True)
            print("le classement est : ")
            for joueur in self.instance_de_tournoi.participants:
                print(joueurs.Joueur.__str__(joueur))
        # Creation des paires
        if len(self.instance_de_tournoi.participants)/2 is int:

            match1 = match.Match(self.instance_de_tournoi.participants[0], self.instance_de_tournoi.participants[4])
            match2 = match.Match(self.instance_de_tournoi.participants[1], self.instance_de_tournoi.participants[5])
            match3 = match.Match(self.instance_de_tournoi.participants[2], self.instance_de_tournoi.participants[6])
            match4 = match.Match(self.instance_de_tournoi.participants[3], self.instance_de_tournoi.participants[7])
            ronde_actuelle = ronde.Ronde("round"+str(numero_ronde),
                                         datetime.datetime.now())
            ronde_actuelle.liste_matchs = [match1, match2, match3, match4]
            # print(ronde_actuelle.__str__())
            return ronde_actuelle

    def deroulement_d_une_ronde(self, numero_de_ronde):
        """ Mécanisme de fonctionnement d'une ronde"""
        # Creation de l'objet instancié tournoi nécessaire
        ronde_actuelle = self.creation_des_matchs_methode_suisse(self, numero_de_ronde)
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
