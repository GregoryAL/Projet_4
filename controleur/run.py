""" Point d'entrée du contrôleur"""
import sys

from modele import tournoi
from modele import match
from modele import ronde
from modele import joueurs
import datetime
import random
from vue.vue import Vue
from controleur.type_de_tournoi import TypeDeTournoi


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
                ronde_actuelle = self.deroulement_d_une_ronde(numero_de_ronde)
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
            joueur_random_key = random.choice(list(self.liste_joueurs.keys()))
            joueur_random = self.liste_joueurs[joueur_random_key]
            self.instance_de_tournoi.participants.append(joueur_random)
            self.liste_joueurs.pop(joueur_random_key)
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

    def deroulement_d_une_ronde(self, numero_de_ronde):
        """ Mécanisme de fonctionnement d'une ronde"""
        # Creation de l'objet instancié tournoi nécessaire
        methode_comptage = TypeDeTournoi("MethodeSuisse", numero_de_ronde, self.instance_de_tournoi)
        print(methode_comptage)
        ronde_actuelle = TypeDeTournoi.creation_des_matchs_methode_suisse(methode_comptage)
        # print(ronde_actuelle)
        # pour chaque match de la liste des matchs de la ronde
        for match_de_ronde in ronde_actuelle.liste_matchs:
            # affiche le match en cours
            print(ronde_actuelle.liste_matchs[match_de_ronde].joueur1.nom + " affronte " +
                  ronde_actuelle.liste_matchs[match_de_ronde].joueur2.nom)
            print("le type de joueur1 est " + str(type(ronde_actuelle.liste_matchs[match_de_ronde].joueur1)))
            # determine un vainqueur
            liste_choix_vainqueur = [str(ronde_actuelle.liste_matchs[match_de_ronde].joueur1.nom),
                                     str(ronde_actuelle.liste_matchs[match_de_ronde].joueur2.nom), "nul"]
            vainqueur = random.choice(liste_choix_vainqueur)
            # modifie les points de tournoi de chaque joueur en fonction du resultat du match
            if vainqueur == str(ronde_actuelle.liste_matchs[match_de_ronde].joueur1.nom):
                print(ronde_actuelle.liste_matchs[match_de_ronde].joueur1.nom + " a gagné contre " +
                      ronde_actuelle.liste_matchs[match_de_ronde].joueur2.nom)
                ronde_actuelle.liste_matchs[match_de_ronde].resultat_joueur1 = 1
                ronde_actuelle.liste_matchs[match_de_ronde].resultat_joueur2 = 0
            elif vainqueur == str(ronde_actuelle.liste_matchs[match_de_ronde].joueur2.nom):
                print(ronde_actuelle.liste_matchs[match_de_ronde].joueur2.nom + " a gagné contre " +
                      ronde_actuelle.liste_matchs[match_de_ronde].joueur1.nom)
                ronde_actuelle.liste_matchs[match_de_ronde].resultat_joueur1 = 0
                ronde_actuelle.liste_matchs[match_de_ronde].resultat_joueur2 = 1
            elif vainqueur == "nul":
                print("C'est un match nul")
                ronde_actuelle.liste_matchs[match_de_ronde].resultat_joueur1 = 0.5
                ronde_actuelle.liste_matchs[match_de_ronde].resultat_joueur2 = 0.5
            ronde_actuelle.liste_matchs[match_de_ronde].joueur1.points_tournoi += \
                ronde_actuelle.liste_matchs[match_de_ronde].resultat_joueur1
            ronde_actuelle.liste_matchs[match_de_ronde].joueur2.points_tournoi += \
                ronde_actuelle.liste_matchs[match_de_ronde].resultat_joueur2
            ronde_actuelle.liste_matchs[match_de_ronde].match = [[ronde_actuelle.liste_matchs[match_de_ronde].joueur1,
                                                                  ronde_actuelle.liste_matchs[match_de_ronde].
                                                                  resultat_joueur1],
                                                                 [ronde_actuelle.liste_matchs[match_de_ronde].joueur2,
                                                                  ronde_actuelle.liste_matchs[match_de_ronde].
                                                                  resultat_joueur2]]
            ronde_actuelle.resultat_matchs = ([ronde_actuelle.liste_matchs[match_de_ronde].joueur1,
                                               ronde_actuelle.liste_matchs[match_de_ronde].resultat_joueur1],
                                               [ronde_actuelle.liste_matchs[match_de_ronde].joueur2,
                                               ronde_actuelle.liste_matchs[match_de_ronde].resultat_joueur2])
        # for participant in liste_de_joueur:
            # print(joueurs.Joueur.__str__(participant))

        return ronde_actuelle


